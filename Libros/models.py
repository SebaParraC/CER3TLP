from django.db import models
# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50,default="",null=True,blank=True)
    genero = models.CharField(max_length=50,default="",null=True,blank=True)
    descripcion = models.CharField(max_length=200,default="",null=True,blank=True)
    precio = models.IntegerField(default=0)
    disponible= models.BooleanField(default=True)
    descuento = models.SmallIntegerField(default=0)
    imagen = models.CharField(max_length=255,default="",null=True,blank=True)

    def __str__(self):
        return self.titulo