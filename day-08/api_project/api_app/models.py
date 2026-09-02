from django.db import models

class SportsCar(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    horsepower = models.IntegerField()
    apple_car_play = models.BooleanField(default=False)
    google_play = models.BooleanField(default=False)
    base_price = models.IntegerField()