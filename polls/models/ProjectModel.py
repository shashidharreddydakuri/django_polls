import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Project(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    # updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title 