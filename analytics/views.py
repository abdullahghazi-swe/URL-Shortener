from django.shortcuts import render
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from main.models import UrlList

# Create your views here.
@login_required
def dashboard(request):
    host = request.build_absolute_uri("/").rstrip("/")

    my_urls = request.user.urls.annotate(clicks=Count('visits'))
    return render(request, 'analytics/dashboard.html', {'urls': my_urls, 'host': host})

@login_required
def link_details(request, url_id):
    host = request.build_absolute_uri("/").rstrip("/")
    link = UrlList.objects.get(id=url_id)
    visits = link.visits.all()
    clicks = len(visits)
    
    return render(request, 'analytics/details.html', {'link': link, 'host': host, 'clicks': clicks})