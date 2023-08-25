from django.db import models
from django.conf import settings

class DailyReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dailyreports', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    