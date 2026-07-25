from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

SUBSCRIPTION_CHOICES = (('free', 'Free'), ('pro', 'Pro'), ('premium', 'Premium'),)

class CustomUser(AbstractUser):

    subscription = models.CharField(max_length=10, choices=SUBSCRIPTION_CHOICES, default='free')

    def __str__(self):
        return self.username