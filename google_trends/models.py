from django.db import models


# Create your models here.
class HistoricalInterestKeyWord(models.Model):
    search_keyword = models.CharField(max_length=250)


class HistoricalInterest(models.Model):
    date_time = models.DateTimeField()
    trends = models.IntegerField()
    is_partial = models.BooleanField()
    search_key = models.ForeignKey(HistoricalInterestKeyWord, on_delete=models.CASCADE, related_name='search_key')


class RegionInterests(models.Model):
    pass
