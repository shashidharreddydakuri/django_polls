import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# from polls.models.BrandsModel import Brand

class Material(models.Model):
        title = models.CharField(max_length=50)
        Description = models.TextField(max_length=100,null=True, blank=True)
        Wc = models.DecimalField(max_digits=6, decimal_places=3, null=True)
        Ri = models.DecimalField(max_digits=6, decimal_places=3, null=True)
        Dk = models.DecimalField(max_digits=6, decimal_places=3, null=True)
        Modulus = models.DecimalField(max_digits=6, decimal_places=3, null=True)
        created = models.DateTimeField(default=timezone.now)
        
        def __str__(self):
            return self.title 