from django.db import models

class Cafe(models.Model):
    cafe = models.CharField(max_length=20)
    
class Drink(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='drinks')
    drink = models.CharField(max_length = 20)
    caffeine = models.IntegerField(default = 0)
