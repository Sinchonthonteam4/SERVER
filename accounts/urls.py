from django.urls import path
from .views import UserAPIView,SignupView,checkDuplicatedEmail,token_refresh
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "users"

urlpatterns = [
    path("refresh/", token_refresh),
    path('signup/',SignupView.as_view(),name='signup'),
    path('login/',UserAPIView.as_view(), name='login'),
    path('check/email/',checkDuplicatedEmail,name='check_email'),
]