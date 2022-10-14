from django.contrib.auth.models import User
from django.db import models

class Sotuvchi(models.Model):
    ism=models.CharField(max_length=30)
    nom=models.CharField(max_length=30)
    manzil=models.CharField(max_length=60)
    tel=models.CharField(max_length=15)
    user=models.ManyToManyField(User,null=True)

    def __str__(self):
        return f"{self.ism}, {self.nom}, ({self.manzil})"
