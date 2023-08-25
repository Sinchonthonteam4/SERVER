from django.core.management.base import BaseCommand
from cafes.models import *

class Command(BaseCommand):
    help = 'Initialize Cafes, Drinks'
    Cafes = [  
        {
            'cafe': 1,
        },  
        {
            'cafe': 2,
        },     
        {
            'cafe': 3,
        },
        {
            'cafe': 4,
        },
    ]

    Drinks = [
        {
            'cafe': 1,
            'drink': '아메리카노',
            'caffeine': 150,
        },
        {
            'cafe': 1,
            'drink': '카라멜 마키아토',
            'caffeine': 75,
        },
        {
            'cafe': 1,
            'drink': '카푸치노',
            'caffeine': 75,
        },
        {
            'cafe': 1,
            'drink': '카페 라떼',
            'caffeine': 75,
        },
        {
            'cafe': 1,
            'drink': '카페 모카',
            'caffeine': 95,
        },
        {
            'cafe': 1,
            'drink': '에스프레소',
            'caffeine': 75,
        },
        {
            'cafe': 1,
            'drink': '얼 그레이 티',
            'caffeine': 50,
        },
        {
            'cafe': 1,
            'drink': '자몽 허니 블랙 티',
            'caffeine': 70,
        },
        {
            'cafe': 1,
            'drink': '자바 칩 프라푸치노',
            'caffeine': 100,
        },
        {
            'cafe': 2,
            'drink': '아메리카노',
            'caffeine': 232,
        },
        {
            'cafe': 2,
            'drink': '카라멜 마키아토',
            'caffeine': 232,
        },
        {
            'cafe': 2,
            'drink': '카푸치노',
            'caffeine': 232,
        },
        {
            'cafe': 2,
            'drink': '카페 라떼',
            'caffeine': 348,
        },
        {
            'cafe': 2,
            'drink': '카페 모카',
            'caffeine': 365,
        },
        {
            'cafe': 2,
            'drink': '에스프레소',
            'caffeine': 116,
        },
        {
            'cafe': 2,
            'drink': '토피넛 라떼',
            'caffeine': 19,
        },
        {
            'cafe': 2,
            'drink': '피치 얼그레이',
            'caffeine': 58,
        },
        {
            'cafe': 2,
            'drink': '아이스티 복숭아',
            'caffeine': 19,
        },
        {
            'cafe': 3,
            'drink': '카페 아메리카노',
            'caffeine': 145,
        },
        {
            'cafe': 3,
            'drink': '콜드브루',
            'caffeine': 196,
        },
        {
            'cafe': 3,
            'drink': '아이스크림 카페라떼',
            'caffeine': 145,
        },
        {
            'cafe': 3,
            'drink': '에스프레소',
            'caffeine': 89,
        },
        {
            'cafe': 3,
            'drink': '달고나 카페라떼',
            'caffeine': 73,
        },
        {
            'cafe': 3,
            'drink': '누가크림 카페라떼',
            'caffeine': 120,
        },
        {
            'cafe': 3,
            'drink': '카라멜 마키아토',
            'caffeine': 177,
        },
        {
            'cafe': 3,
            'drink': '로얄 밀크티',
            'caffeine': 101,
        },
        {
            'cafe': 3,
            'drink': '카푸치노',
            'caffeine': 177,
        },
        {
            'cafe': 4,
            'drink': '에너지드링크',
            'caffeine': 58,
        }
    ]
    def handle(self, *args, **options):
        for cafe in self.Cafes:
            Cafe.objects.get_or_create(
                cafe = cafe['cafe'], 
            )
            
        for drink in self.Drinks:
            Drink.objects.get_or_create(
                cafe = Cafe.objects.get(id=drink['cafe']),
                drink = drink['drink'],
                caffeine = drink['caffeine']
            )
                        
        self.stdout.write(self.style.SUCCESS('Drinks initialized'))
        return 0
            