import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

from polls.models.BrandsModel import Brand

class BaseCurve(models.Model):
    BCvalue = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class DIACurve(models.Model):
    DIAvalue = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
