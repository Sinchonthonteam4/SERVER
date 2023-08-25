from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', DailyReportCreateListView.as_view()),
    path('daily/',DailyReportAPIView.as_view()),
    path('<int:pk>',DailyReportRetrieveDestroyView.as_view()),
    path('challenge/', ListAPIView.as_view()),
]