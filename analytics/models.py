from django.db import models

# Create your models here.

class Visit(models.Model):
    url = models.ForeignKey('main.UrlList', on_delete=models.CASCADE, related_name='visits')
    referrer = models.URLField(null=True)
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, null=True)
    browser = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    is_bot = models.BooleanField(default=False)
    visited_at = models.DateTimeField(auto_now_add=True)