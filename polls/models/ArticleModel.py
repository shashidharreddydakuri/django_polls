import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

from .PublicationModel import Publication

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline