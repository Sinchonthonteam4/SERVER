from rest_framework import serializers

from .models import DailyReport
from cafes.models import Drink, Cafe
from accounts.models import University, User

import datetime

class DailyReportCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DailyReport
        fields = '__all__'
        

class DailyReportSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_nickname = serializers.CharField(source='user.nick_name',read_only=True)
    class Meta:
        model = DailyReport
        fields = ['user','user_nickname','total']
        depth = 1

# WeekReport
class WeekReportSerilizer(serializers.ModelSerializer):
    pass