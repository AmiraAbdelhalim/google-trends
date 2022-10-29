from django.contrib import admin
from .models import HistoricalInterest, HistoricalInterestKeyWord, RegionInterests

# Register your models here.
admin.site.register(HistoricalInterest)
admin.site.register(HistoricalInterestKeyWord)
admin.site.register(RegionInterests)
