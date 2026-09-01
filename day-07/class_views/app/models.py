from django.db import models

class GamingPC(models.Model):
    ram = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200)
    gpu = models.CharField(max_length=200)