from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', DailyReportCreateListView.as_view()),
    path('daily/',DailyReportAPIView.as_view()),
]