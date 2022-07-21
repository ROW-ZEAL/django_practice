from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class car(models.Model):
    car_model = (
        ('M', 'Mercedes-Benz'),
        ('T', 'Tesla'),
        ('L', 'Lamborghini'),
    )
    name = models.CharField(max_length=60)
    car_chose = models.CharField(max_length=1, choices=car_model)




class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

class Artist(models.Model):
    name = models.CharField(max_length=10)
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)