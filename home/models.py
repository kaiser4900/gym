from django.db import models
from django.contrib.auth.models import AbstractUser

class Niveles(models.Model):
    name_nivel = models.CharField(max_length = 20,unique=True)
    description = models.CharField(max_length= 50)
 
    def __str__(self):
        return self.name_nivel

class User(AbstractUser):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    level = models.ForeignKey(Niveles,on_delete=models.DO_NOTHING)
    dni = models.PositiveIntegerField()
    email = models.EmailField()
    image = models.ImageField(null=False, upload_to='img/users')
    isAdmin = models.BooleanField(default=False)

class Normal_Admin(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    direccion = models.CharField(max_length=100)



class Usuario(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    peso = models.FloatField()
    altura = models.FloatField()   
    direccion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombres+ " " + self.apellidos

class Entrenado(models.Model):
    id_usuario = models.FileField.unique=True
    fecha = models.DateTimeField(auto_now_add=True)
    entrenado = models.BooleanField(default=False)


    def __str__(self) -> str:
        return str(int(self.id_usuario)) + " "+ str(self.fecha)+' '+str(self.entrenado)