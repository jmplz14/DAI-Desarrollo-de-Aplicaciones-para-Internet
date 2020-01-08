from django.db import models

# Create your models here.
class Grupo(models.Model):
    nombre = models.CharField(max_length=200, primary_key=True)
    fechaCreacion = models.DateField()
    estilo = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=200)
    distribuidora = models.CharField(max_length=200)
    fechaLanzamiento = models.DateField()
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)


class Musico(models.Model):
    nombre = models.CharField(max_length=200)
    fechaNacimiento = models.DateField()
    instrumentoPrincipal = models.CharField(max_length=200)
    grupo = models.ManyToManyField(Grupo)
    edad = models.IntegerField()
    coordenadaX = models.FloatField()
    coordenadaY = models.FloatField()

    def __str__(self):
        return self.nombre


