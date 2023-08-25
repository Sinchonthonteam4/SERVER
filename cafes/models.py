from django.db import models

class Cafe(models.Model):
    cafe = models.CharField(max_length=20)
    
    def __str__(self):
        return self.cafe
    
    
class Drink(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='drinks')
    drink = models.CharField(max_length = 20)
    caffeine = models.IntegerField(default = 0)
    
    def __str__(self):
        return f'{self.cafe}의 {self.drink}' 