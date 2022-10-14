from django.db import models
from user.models import *
from asosiy.models import *

class Statistika(models.Model):
    mahsulot=models.ForeignKey(Mahsulot,on_delete=models.CASCADE, null=True)
    mijoz=models.ForeignKey(Mijoz,on_delete=models.CASCADE, null=True)
    miqdor=models.CharField(max_length=50)
    sana=models.DateField()
    sotuvchi=models.ForeignKey(Sotuvchi,on_delete=models.CASCADE, null=True)
    jami=models.IntegerField()
    tolandi=models.IntegerField()
    nasiya=models.IntegerField()

    def __str__(self):
        return self.mahsulot.nom