import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

from .ProjectModel import Project
from .ManufacturerModel import Manufacturer
from .MaterialModel import Material

class Lens(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    
    # created = models.DateTimeField(default=timezone.now)
    # updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title 

        