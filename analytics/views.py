from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import UrlList

# Create your views here.
@login_required
def dashboard(request):
    my_urls = UrlList.objects.filter(created_by = request.user)
    return render(request, 'analytics/dashboard.html')