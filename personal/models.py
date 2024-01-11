from django.db import models
from catalogos.models import Rango
from home.models import ClaseBase

# Create your models here.
class Personal(ClaseBase):
    rango = models.ForeignKey(Rango, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10, help_text='', unique=True)
    nombres_apellidos = models.CharField(max_length=20, help_text='')
    f_nac = models.DateField()
    t_sangre = models.CharField(max_length=20, help_text='')
    ciudad_nacimiento = models.CharField(max_length=20, help_text='')
    celular = models.CharField(max_length=10, help_text='')

    def __str__(self):
        return '{}:{}'.format(self.rango, self.nombres_apellidos)

    def save(self, *args, **kwargs):
        self.nombres_apellidos = self.nombres_apellidos.upper()
        self.t_sangre = self.t_sangre.upper()
        self.ciudad_nacimiento = self.ciudad_nacimiento.upper()
        # Agrega las demás conversiones a mayúsculas para los campos necesarios
        super(Personal, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Personal Policial"

