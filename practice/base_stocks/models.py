from pstats import StatsProfile
import sqlite3
from telnetlib import STATUS
from django.db import models

# Create your models here.
class Stock(models.Model):
    Stock_name = models.CharField(max_length=30)
    Symbol = models.CharField(max_length=30)
    Sctor_id = models.IntegerField(max_length=30)
    Stauts = models.IntegerField()



