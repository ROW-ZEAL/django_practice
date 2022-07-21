from turtle import clear
from django.db import models

# Create your models here.
class sector(models.Model):
    sector_name = models.CharField(max_length=30)

