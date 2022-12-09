from django.db import models

class Deporte(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="deportes",null=True,blank=True)

class Articulo(models.Model):
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2,max_digits=10,)
    publicacion = models.DateField()
    imagen = models.ImageField(upload_to="articulos",null=True,blank=True)
