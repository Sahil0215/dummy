from django.db import models

# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=15)