from rest_framework.serializers import ModelSerializer
from .models import Cafe, Drink

class CafeSerializer(ModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'

class DrinkSerializer(ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'