from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import DailyReport
from cafes.models import Cafe, Drink
from .serializers import DailyReportSerializer, DailyReportCreateSerializer

class DailyReportCreateListView(generics.ListCreateAPIView):
    queryset = DailyReport.objects.all()

    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return DailyReportSerializer
        return DailyReportCreateSerializer
    
    def create(self, request, *args, **kwargs):
        drink_id = request.data['drink']
        cups = request.data['cups']
        drink = Drink.objects.get(id=drink_id)
        
        total =  int (drink.caffeine) * int(cups)
        dr = {
            'drink' : drink_id,
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
