from django.db import models

# Create your models here.

class Gato(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField(null=True)
    
class persona_responsable(models.Model):
    nombre_persona=models.CharField(max_length=20)
    edad_persona=models.IntegerField()
    dni=models.IntegerField()
    
class ubicacion(models.Model): 
    direccion=models.CharField(max_length=50)
    pais=models.CharField(max_length=15)
    codigo_postal=models.IntegerField()
    