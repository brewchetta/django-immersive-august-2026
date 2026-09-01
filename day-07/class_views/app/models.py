from django.db import models

class GamingPC(models.Model):
    ram = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200)
    gpu = models.CharField(max_length=200)


class Headphone(models.Model):
    brand = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=7)