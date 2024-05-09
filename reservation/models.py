from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Reservation(models.Model):
    nom = models.CharField(max_length=50)
    email = models.EmailField()
    téléphone = models.IntegerField()
    nombre_de_personnes = models.IntegerField()
    Date = models.DateField()
    temps= models.TimeField()
    



    def __str__(self):
        return self.nom