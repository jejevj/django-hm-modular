# modules/models.py

from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url_path = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=10, default='1.0')

    def __str__(self):
        return self.name
