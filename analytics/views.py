from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import UrlList

# Create your views here.
@login_required
def dashboard(request):
    host = request.build_absolute_uri("/").rstrip("/")

    my_urls = request.user.urls.all()
    return render(request, 'analytics/dashboard.html', {'urls': my_urls, 'host': host})