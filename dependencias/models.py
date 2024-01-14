from django.db import models
from home.models import ClaseBase

# Create your models here.
#Modelo de Provincia
class Provincia(ClaseBase):
    codigo = models.CharField(
        max_length=10,
        help_text='',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Provincia, self).save()

    class Meta:
        verbose_name_plural = "Provincias"

    
class Distrito(ClaseBase):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=10,
        help_text='',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='',
        unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.provincia,self.codigo)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Distrito, self).save()

    class Meta:
        verbose_name_plural = "Distritos"
        unique_together = ('codigo','nombre')

class Canton(ClaseBase):
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=10,
        help_text='',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='',
        unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.distrito.codigo,self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Canton, self).save()

    class Meta:
        verbose_name_plural = "Cantones"
        unique_together = ('codigo','nombre')

class Circuito(ClaseBase):
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=10,
        help_text='',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='',
        unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.canton.nombre,self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Circuito, self).save()

    class Meta:
        verbose_name_plural = "Circuitos"
        unique_together = ('codigo','nombre')

class Subcircuito(ClaseBase):
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    codigo = models.CharField(
        max_length=12,
        help_text='',
        unique=True
    )
    nombre = models.CharField(
        max_length=30,
        help_text='',
        unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.circuito.codigo,self.codigo)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Subcircuito, self).save()

    class Meta:
        verbose_name_plural = "Subcircuitos"
        unique_together = ('codigo','nombre')