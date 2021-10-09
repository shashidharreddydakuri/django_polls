import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Kelvin(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title




