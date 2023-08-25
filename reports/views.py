from django.shortcuts import render
from django.core.exceptions import ValidationError

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.views import APIView


from .models import DailyReport
from cafes.models import Cafe, Drink
from .serializers import DailyReportSerializer, DailyReportCreateSerializer
from accounts.models import User
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError 

from datetime import *

class DailyReportCreateListView(generics.ListCreateAPIView):
    queryset = DailyReport.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return DailyReportSerializer
        return DailyReportCreateSerializer
    
    def create(self, request, *args, **kwargs):
        drink_name = request.data['drink']
        cups = request.data['cups']
        cafe_name = request.data['cafe']
        cafe = Cafe.objects.get(cafe=cafe_name).id
        drink = Drink.objects.get(drink=drink_name,cafe=cafe).id
        user = request.user.id
        
        
        total =  int (drink.caffeine) * int(cups)
        dr = {
            'user': user,
            'drink' : drink,
            'cups' : cups,
            'total' : total
        }
        
        serializer = self.get_serializer(data= dr)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



# DailyReport 수정, 삭제, 조회
class DailyReportRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer
    
    permission_classes = [IsAuthenticated]
    
class DailyReportAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        reports = DailyReport.objects.filter(user=request.user)
        data = DailyReportSerializer(instance=reports.last()).data
        data['diff'] = data['total']-400
        data['user_email'] = str(data['user_email']).split('@')[0]
        data.pop('total')
        data.pop('user')


# Week Report
class WeekReportAPIView(generics.ListAPIView):
    queryset = DailyReport.objects.all()
    def get(self, request):
        queryset = DailyReport.objects.filter(date__gte= datetime.now()-timedelta(weeks=1),user=request.user)
    
        total = 0
        average = 0
        cnt = 0
        cups = 0
        for query in queryset:
            total += int(query.total)
            cnt += 1
            cups += int(query.cups)
        if cnt>0:
            average = total / cnt
        else:
            average = 0
        compare = total - 2800
        money = 4000 * cups
        data =  {
                    'total': total,
                    'average': average,
                    'compare': compare,
                    'money': money
                }
        return Response(data,status=status.HTTP_200_OK)
        
 
