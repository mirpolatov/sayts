from django.db import models

# Create your models here.


class Asosiy(models.Model):
    images = models.ImageField(upload_to='images/')

class Konsert(models.Model):
    dastur_nomi = models.CharField(max_length=50,null=True,blank=True)
    avtor = models.CharField(max_length=50,null=True,blank=True)
    link = models.URLField()


class Kliplar(models.Model):
    klip_nomi = models.CharField(max_length=50,null=True,blank=True)
    avtor = models.CharField(max_length=50,null=True,blank=True)
    link = models.URLField()


class Toplamlar(models.Model):
    toplam_nomi = models.CharField(max_length=50,null=True,blank=True)
    avtor = models.CharField(max_length=50,null=True,blank=True)
    link = models.URLField()

class AsosiyBolimIjorchi(models.Model):
    nomi = models.CharField(max_length=50,null=True,blank=True)
    avtor = models.CharField(max_length=50,null=True,blank=True)
    link = models.URLField()


