from django.db import models


# Create your models here.
class Usuario(models.Model):
    nickname = models.CharField(primary_key= True, max_length=20) 
    nombre_apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)


class Cancion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class lista_reproduccion(models.Model): 
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class lista_cancion(models.Model):
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    lista_reproduccion = models.ForeignKey(lista_reproduccion, on_delete=models.CASCADE)



