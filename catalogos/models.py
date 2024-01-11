from django.db import models
from home.models import ClaseBase

# Create your models here.
#Modelo para clase Rango de catalogos
class Rango(ClaseBase):
    nombre = models.CharField(
        max_length=20,
        help_text='',
        unique=True
    )
    
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Rango, self).save()

    class Meta:
        verbose_name_plural = "Rangos"

#Modelo para clase Tipo de Vehiculo de catalogos
class Tipo_Vehiculo(ClaseBase):
    nombre = models.CharField(
        max_length=15,
        help_text='',
        unique=True
    )
    
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Tipo_Vehiculo, self).save()

    class Meta:
        verbose_name_plural = "Tipos_Vehiculos"

#Modelo para clase Tipo de Mantenimiento de catalogos
class Tipo_Mantenimiento(ClaseBase):
    nombre = models.CharField(
        max_length=20,
        help_text='',
        unique=True
    )
    
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Tipo_Mantenimiento, self).save()

    class Meta:
        verbose_name_plural = "Tipos_Mantenimientos"
