from django.urls import path
from .views import search_trends, get_historical_interests_data

urlpatterns = [
    path('', search_trends, name="search_trends"),
    path('trends/<str:search_keyword>', get_historical_interests_data, name="historical_interests")
]