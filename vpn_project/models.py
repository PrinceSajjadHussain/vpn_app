from django.db import models
from django.contrib.auth.models import User

class VPNUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, default='US')  # Store the selected country
    config_file = models.TextField(blank=True, null=True)    # Store the generated config file
