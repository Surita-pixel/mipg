from django import forms
from . import models


class OficinaForm(forms.ModelForm):
    class Meta:
        model = models.Oficina
        fields = [
            "nombre_oficina",
        ]
