from django.urls import path
from .views import search_trends

urlpatterns = [
    path('', search_trends, name="search_trends")
]