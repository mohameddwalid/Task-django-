from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=60)
    quantity = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    invname = models.CharField(max_length=60)


class Inventories(models.Model):
    name = models.CharField(max_length=60)
    capacity = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    


