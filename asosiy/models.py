from django.db import models

from user.models import *


class Mahsulot(models.Model):
    nom=models.CharField(max_length=50)
    brend=models.CharField(max_length=50)
    miqdor=models.PositiveSmallIntegerField()
    narx=models.PositiveSmallIntegerField()
    olchov=models.CharField(max_length=50)
    kelgan_sana=models.DateTimeField(auto_now_add=True)
    sotuvchi=models.ForeignKey(Sotuvchi,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nom} , {self.sotuvchi}'
class Mijoz(models.Model):
    ism=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    manzil=models.CharField(max_length=50)
    tel=models.CharField(max_length=50)
    qarz=models.PositiveIntegerField()
    sotuvchi=models.ForeignKey(Sotuvchi,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.ism},{self.nom}, ({self.manzil})'

