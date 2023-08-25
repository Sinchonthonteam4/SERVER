from django.core.management.base import BaseCommand
from accounts.models import *

class Command(BaseCommand):
    help = 'Initialize Cafes, Drinks'
    Universities = [  
        {
            'univ_name': '서강대학교',
            'location': '신촌',
        },  
        {
            'univ_name': '연세대학교',
            'location': '신촌',
        },     
        {
            'univ_name': '이화여자대학교',
            'location': '신촌',
        },
        {
            'univ_name': '홍익대학교',
            'location': '신촌',
        },
    ]

    
    def handle(self, *args, **options):
        for university in self.Universities:
            University.objects.get_or_create(
                univ_name = university['univ_name'],
                location = university['location'],
            )
                        
        self.stdout.write(self.style.SUCCESS('University initialized'))
        return 0
            