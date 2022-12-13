from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    website = models.URLField(max_length=50, blank=True)