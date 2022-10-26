from django.shortcuts import render


# Create your views here.
def search_trends(request):
    return render(request, 'google_trends/trends.html', {})
