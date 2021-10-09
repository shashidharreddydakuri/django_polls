import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# from polls.models.BrandsModel import Brand

class Manufacturer(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    # brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    # updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title 
    