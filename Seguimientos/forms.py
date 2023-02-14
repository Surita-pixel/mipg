from django import forms
from Seguimientos.models import Formulario_Seguimiento
from Departamentos.models import Oficina
from Formularios.models import Formulario
from Planes.models import Plan
from . import models


class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = models.Seguimiento
        fields = [
            "seguimiento_formulario_pivot",
            "oficina",
        ]

    def __init__(self, *args, **kwargs):
        super(SeguimientoForm, self).__init__(*args, **kwargs)
        self.fields["seguimiento_formulario_pivot"].queryset = Formulario_Seguimiento.objects.all()
        self.fields["oficina"].queryset = Oficina.objects.all()



class Formulario_SeguimientoForm(forms.ModelForm):
    class Meta:
        model = models.Formulario_Seguimiento
        fields = [
            "formulario_seguimiento",
            "Formulario_Seguimiento",
            "Formulario_Seguimiento_Plan",
        ]

    def __init__(self, *args, **kwargs):
        super(Formulario_SeguimientoForm, self).__init__(*args, **kwargs)
        self.fields["Formulario_Seguimiento"].queryset = Formulario.objects.all()
        self.fields["Formulario_Seguimiento_Plan"].queryset = Plan.objects.all()

