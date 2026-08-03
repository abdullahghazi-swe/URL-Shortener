from django.db import models
from django.conf import settings

# Create your models here.

class UrlList(models.Model):
    input_url = models.CharField(max_length=1000)
    shorten = models.CharField(max_length=10, unique=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='urls')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shorten