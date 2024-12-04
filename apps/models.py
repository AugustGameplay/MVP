from django.db import models

# Create your models here.
# Modelo simple para los usuarios
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
