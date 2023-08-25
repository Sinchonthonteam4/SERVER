from django.contrib import admin
from .models import Cafe, Drink

admin.site.register(Cafe)
admin.site.register(Drink)

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cafe)
admin.site.register(Drink)
