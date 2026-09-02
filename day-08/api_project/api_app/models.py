from django.db import models

class SportsCar(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    horsepower = models.IntegerField()
    apple_car_play = models.BooleanField(default=False)
    google_play = models.BooleanField(default=False)
    base_price = models.IntegerField()


from django.core.validators import MinValueValidator, MaxValueValidator

class TradingCard(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    rarity = models.CharField(max_length=200)
    description = models.TextField()
    psa_grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


class Phone(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)


class Channel(models.Model):
    name = models.CharField(max_length=200)
    cable = models.BooleanField()