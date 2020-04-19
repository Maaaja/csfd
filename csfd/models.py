from django.db import models

# Create your models here.

class Filmy(models.Model):
    nazev = models.CharField(max_length=100)
    rok = models.IntegerField()
    url = models.CharField(max_length=100)
    hodnoceni = models.CharField(max_length=6)
    tvurci = models.ManyToManyField('Tvurci')


class Tvurci(models.Model):
    jmeno = models.CharField(max_length=100)
    id_tvurce = models.CharField(max_length=100)

class Idecka(models.Model):
    id_tvurce = models.CharField(max_length=100)
    id_filmu = models.IntegerField()