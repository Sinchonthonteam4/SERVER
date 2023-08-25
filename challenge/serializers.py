# from rest_framework import serializers

# from reports.models import DailyReport
# from cafes.models import Drink, Cafe
# from accounts.models import University, User

# import datetime
# class MonthReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = DailyReport
#         fields = '__all__'
        
# class ChallengeSerializer(serializers.ModelSerializer):
#     reports = serializers.SerializerMethodField()
#     class Meta:
#         model = DailyReport
#         fields = ['id', 'user', 'total']
#     def get_reports_queryset(self, univ_id):
#         user_id = User.objects.filter(university=univ_id)
#         reports = DailyReport.objects.filter(user = user_id)
#         return reports
    
#     def get_reports(self, univ_id):
#         year = datetime.datetime.now().year 
#         month = datetime.datetime.now().month #오늘 
#         first_date = datetime.date(year, month, 1)
#         last_date = datetime.date(year, month, 28)
#         print(year, month, first_date, last_date)
#         queryset = self.get_reports_queryset(univ_id).filter(date__range = (first_date,last_date))
#         return MonthReportSerializer(queryset, many=True).data