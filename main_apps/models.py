# modules/models.py

from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url_path = models.CharField(
        max_length=255,
        unique=True,
        help_text="Url path sudah digunakan, harus unik. hanya huruf kecil, angka, hyphens (-), dan slashes (/) yang diperbolehkan."
    )
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=10, default='1.0')
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.name
