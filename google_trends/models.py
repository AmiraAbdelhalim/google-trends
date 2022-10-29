from django.db import models


# Create your models here.
class HistoricalInterestKeyWord(models.Model):
    search_keyword = models.CharField(max_length=250)

    def __str__(self):
        return self.search_keyword


class HistoricalInterest(models.Model):
    date_time = models.DateTimeField()
    trends = models.IntegerField()
    is_partial = models.BooleanField()
    search_key = models.ForeignKey(HistoricalInterestKeyWord, on_delete=models.CASCADE, related_name='search_key')

    def __str__(self):
        return self.trends


class RegionInterests(models.Model):
    keyword1 = models.CharField(max_length=250, null=True)
    keyword2 = models.CharField(max_length=250, null=True)
    region = models.CharField(max_length=250, null=True)
    trends = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.keyword1} {self.keyword2}'
