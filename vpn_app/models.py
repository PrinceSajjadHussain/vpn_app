from django.db import models
from django.contrib.auth.models import User

class VPNUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, default='US')
    config_file = models.TextField(blank=True, null=True)
    is_enabled = models.BooleanField(default=False)  # Add the is_enabled field
