from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from cafes.models import Cafe, Drink

class Command(BaseCommand):
    help = 'Crawl Starbucks drink data and save to the database'

    def handle(self, *args, **options):
        url = "https://www.starbucks.co.kr/menu/drink_list.do"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find drink information on the page
        drink_tables = soup.find_all("table", class_="coffeInfo mb60")

        # Loop through the drink list
        for drink_table in drink_tables:
            try:
                drink_list = drink_table.find("tbody")
                rows = drink_list.find_all("tr")
                
                for row in rows:
                    drink_name = row.find_all("td")[0].get_text(strip=True)
                    caffeine_info = row.find_all("td")[-1].get_text(strip=True)

                # Create or update the Cafe entry
                cafe, created = Cafe.objects.get_or_create(cafe="Starbucks")

                # Create a new Drink entry
                drink, created = Drink.objects.get_or_create(
                    cafe=cafe,
                    drink=drink_name,
                    caffeine=caffeine_info
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added "{drink_name}" to the database.'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated "{drink_name}" in the database.'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing item: {str(e)}'))