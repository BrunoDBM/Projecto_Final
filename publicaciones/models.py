from django.db import models

# Create your models here.
class Publicacion(models.Model):
    fecha = models.DateField(max_length=True)
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    categoria = models.CharField(max_length=50)
    creador = models.CharField(max_length=50)

def __str__