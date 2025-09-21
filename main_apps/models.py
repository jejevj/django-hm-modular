# modules/models.py
from django.db import models
from .utils.barcode import generate_barcode_base64  

class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url_path = models.CharField(
        max_length=255,
        unique=True,
    )
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=10, default='1.0')
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.name

class NamaProduct(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, unique=True)
    barcode = models.TextField(unique=True, blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.barcode or self._state.adding:
            self.barcode = generate_barcode_base64(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

