from django.db import models

class Niveles(models.Model):
    nivel = models.CharField(max_length = 10)
 
    def __str__(self):
        return self.nivel

class Usuario(models.Model):
    nombre_usuario =  models.CharField(max_length=30)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    nivel = models.PositiveIntegerField()
    dni = models.PositiveIntegerField()
    peso = models.FloatField()
    altura = models.FloatField()   
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    image = models.ImageField(null=False, upload_to='static/assets/img/profile/')

    def __str__(self):
        return self.nombres+ " " + self.apellidos

class Entrenado(models.Model):
    id_usuario = models.FileField.unique=True
    fecha = models.DateTimeField(auto_now_add=True)
    entrenado = models.BooleanField(default=False)


    def __str__(self) -> str:
        return str(int(self.id_usuario)) + " "+ str(self.fecha)+' '+str(self.entrenado)