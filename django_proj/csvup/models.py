from unicodedata import name
from django.db import models

class Product(models.Model):
    name = models.CharField("Name",max_length=255)
    sku = models.CharField("SKU",max_length=255,unique=True)
    desc = models.CharField("Description",max_length=500)

def __str__(self):
    return self.name