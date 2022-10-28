from django.contrib import admin
from .models import HistoricalInterest, HistoricalInterestKeyWord

# Register your models here.
admin.site.register(HistoricalInterest)
admin.site.register(HistoricalInterestKeyWord)
