from django.urls import path
from .views import search_trends, get_historical_interests_data, search_region, get_regions_data

urlpatterns = [
    path('', search_trends, name="search_trends"),
    path('trends/<str:search_keyword>', get_historical_interests_data, name="historical_interests"),
    path('region', search_region, name="search_region"),
    path('regions/<str:kw1>/<str:kw2>', get_regions_data, name="interested_regions"),

]