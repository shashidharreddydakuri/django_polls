import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=30)
    cover = models.ImageField(upload_to='images/')
    # kelvin = models.ForeignKey(Kelvin, on_delete=models.CASCADE)

    def __str__(self):
        return self.title      




