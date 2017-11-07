from django import forms

from apps.pedido_prestamo.models import Prestamo


class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo

        fields = [
            "dni",
            "nombre",
            "apellido",
            "genero",
            "email",
            "monto",
        ]

        labels = {
            "dni": "DNI",
            "nombre": "Nombre",
            "apellido": "Apellido",
            "genero": "Genero",
            "email": "E-mail",
            "monto": "Monto",
        }

        widgets = {
            "dni": forms.NumberInput(attrs={'min': 0,
                                            'max': 99999999,
                                            'class': "form-control"}),
            "nombre": forms.TextInput(attrs={'class': "form-control"}),
            "apellido": forms.TextInput(attrs={'class': "form-control"}),
            "genero": forms.Select(attrs={'class': "form-control"}),
            "email": forms.EmailInput(attrs={'class': "form-control"}),
            "monto": forms.NumberInput(attrs={'min': 1000,
                                              'max': 1000000,
                                              'class': "form-control"}),
        }
