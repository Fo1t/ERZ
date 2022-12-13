from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)
    

class District(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='district_region')
    

class Settlement(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='settlement_district')


class Street(models.Model):
    name = models.CharField(max_length=50)
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE, related_name='street_settlement')