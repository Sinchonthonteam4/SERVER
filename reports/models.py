from django.db import models
from django.conf import settings
from cafes.models import Drink

class DailyReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dailyreports', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, null=True, blank=True, related_name='dailyreports')
    cups = models.IntegerField(default = 1)
    total = models.IntegerField(default = 100)
    
    def __str__(self):
        return f'총 카페인 섭취량: {self.total} 음료: {self.drink}'
        
