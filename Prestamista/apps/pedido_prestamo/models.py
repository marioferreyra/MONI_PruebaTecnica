from django.db import models

from django.core.validators import RegexValidator
# Create your models here.


class Prestamo(models.Model):
    MASCULINO = "M"
    FEMENINO = "F"

    GENEROS = ((MASCULINO, "Masculino"),
               (FEMENINO, "Femenino"),
               )

    alphanumeric = RegexValidator(r'^[a-zA-Z]*$',
                                  'Only alphabetic characters are allowed.')

    dni = models.IntegerField()
    nombre = models.CharField(max_length=20, validators=[alphanumeric])
    apellido = models.CharField(max_length=20, validators=[alphanumeric])
    genero = models.CharField(max_length=20, choices=GENEROS,
                              default=MASCULINO)
    email = models.EmailField(max_length=254)
    monto = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)
