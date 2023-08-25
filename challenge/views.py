from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response 
from reports.models import DailyReport
from cafes.models import Cafe, Drink
from accounts.models import User, University
from reports.serializers import DailyReportCreateSerializer

from datetime import datetime, date

class ChallengeListAPIView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = DailyReportCreateSerializer
    def get(self, request):
        data = []
        for query in self.get_queryset():
            univ_id = query.id
            users = User.objects.filter(university=univ_id)
            year = datetime.now().year 
            month = datetime.now().month #오늘 
            first_date = date(year, month, 1)
            last_date = date(year, month, 28)
            print(year, month, first_date, last_date)
            queryset = DailyReport.objects.filter(date__range = (first_date,last_date))
            
            univ_caffeine = 0
            for query in queryset:
                if (query.user in users):
                    univ_caffeine += query.total
            univ = University.objects.get(id=univ_id)
            data.append({
                'university': univ.univ_name,
                'univ_caffeine': univ_caffeine
            })
            #  대학 이름, 카페인 양
        data.sort(key=lambda x: -x['univ_caffeine'])
        return Response(data,status=status.HTTP_200_OK)