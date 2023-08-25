from rest_framework import serializers
from .models import DailyReport
from cafes.models import Drink, Cafe

class DailyReportCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DailyReport
        fields = '__all__'
        

class DailyReportSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_email = serializers.CharField(source='user.email',read_only=True)
    class Meta:
        model = DailyReport
        fields = ['user','user_email','total']
        depth = 1
    
class WeekReportSerializer(serializers.ModelSerializer):
    pass