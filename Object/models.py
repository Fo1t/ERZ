from django.db import models
from Developer.models import Developer
from Areal.models import Region, Settlement, Street, District

class Date(models.Model):
    QUARTER_TYPES = [
        ('1', 'I кв.'),
        ('2', 'II кв.'),
        ('3', 'III кв.'),
        ('4', 'IV кв.'),
    ]
    quarter = models.CharField(max_length=1, choices=QUARTER_TYPES, default='I')
    year = models.PositiveSmallIntegerField(blank=False)
    
    def __str__(self):
        return f'{self.year} {self.quarter}'


class General(models.Model):
    name = models.CharField(max_length=50)
    type_of_development_group =  models.CharField(max_length=50)
    brand = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='general_developer')
    military_mortgage = models.BooleanField(default=False)
    maternity_capital = models.BooleanField(default=False)
    start_of_residential_complex_construction = models.ForeignKey(Date, null=True, on_delete=models.SET_NULL, related_name='general_date_start')
    end_of_residential_complex = models.ForeignKey(Date, null=True, on_delete=models.SET_NULL, related_name='general_date_end')
    address = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f'{self.name} {self.brand.name}'
    

class Object(models.Model):
    name = models.CharField(max_length=50)
    general = models.ForeignKey(General, on_delete=models.CASCADE, related_name='object_general')
    state = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f'{self.name} {self.street}'
    
class Apartment(models.Model):
    TYPES = [
        ('0', 'Студия'),
        ('1', '1-комнатная'),
        ('2', '2-комнатная'),
        ('3', '3-комнатная'),
        ('4', '4-комнатная'),
        ('5', '5-комнатная'),
        ('6', '6-комнатная'),
        ('7', 'Многокомнатная'),
    ]
    rooms = models.CharField(max_length=1, choices=TYPES, default='0')
    min_square = models.FloatField(default=0.0)
    max_square = models.FloatField(default=0.0)
    min_cost = models.FloatField(default=0.0)
    max_cost = models.FloatField(default=0.0)
    count = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=50)
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='apartment_object')