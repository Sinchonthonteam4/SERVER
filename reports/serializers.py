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
    class Meta:
        model = DailyReport
        fields = '__all__'
        depth = 1

# WeekReport
class WeekReportSerilizer(serializers.ModelSerializer):
    pass