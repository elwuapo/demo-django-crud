from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Raza(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Perro(models.Model):
    nro_chip = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=99)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE) #eliminacion en casacada.

    def ruta_imagen(self, filename):
        return f'perros/{self.nro_chip}/imagenes/{filename}'

    imagen = models.ImageField(upload_to = ruta_imagen, null = True, blank = True)

class Cuenta(models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    perros_adoptados = models.ManyToManyField(Perro)
    fecha_ultima_adopcion = models.DateField()
    fecha_login = models.DateTimeField()
    notificar = models.BooleanField()


