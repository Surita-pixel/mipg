from django import forms
from Formularios.models import Formulario
from Departamentos.models import Oficina
from . import models


class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = models.Seguimiento
        fields = [
            "seguimiento_formulario",
            "oficina",
        ]

    def __init__(self, *args, **kwargs):
        super(SeguimientoForm, self).__init__(*args, **kwargs)
        self.fields["seguimiento_formulario"].queryset = Formulario.objects.all()
        self.fields["oficina"].queryset = Oficina.objects.all()

