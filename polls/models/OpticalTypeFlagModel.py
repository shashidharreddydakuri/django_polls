import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class OpticalTypeFlag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title 