import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# from polls.models.MaterialModel import Material
# from polls.models.ProjectModel import Project
# from polls.models.ManufacturerModel import Manufacturer

class Brand(models.Model):
    title = models.CharField(max_length=30)
    Description = models.TextField(max_length=100,null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # material = models.ForeignKey(Material, on_delete=models.CASCADE)
    # material = models.ForeignKey(Material, on_delete=models.CASCADE)
    def __str__(self):
        return self.title