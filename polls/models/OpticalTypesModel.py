import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

from .OpticalTypeFlagModel import OpticalTypeFlag
# from polls.models.BrandsModel import Brand

class OpticalTypes(models.Model):
    title = models.CharField(max_length=30)
    opticaltypeflags = models.ManyToManyField(OpticalTypeFlag)
    # brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    def __str__(self):
        return self.title