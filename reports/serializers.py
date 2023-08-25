from rest_framework import serializers
from .models import DailyReport, Drink

class DailyReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = '__all__'
        

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = '__all__'
        depth = 1
    