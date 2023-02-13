from django import forms
from Departamentos.models import Plan
from Formularios.models import Formulario
from Seguimientos.models import Formulario_Seguimiento
from Departamentos.models import Oficina
from . import models


class Formulario_SeguimientoForm(forms.ModelForm):
    class Meta:
        model = models.Formulario_Seguimiento
        fields = [
            "seguimiento_name",
            "Formulario_Seguimiento_Plan",
            "Formulario_Seguimiento",
        ]

    def __init__(self, *args, **kwargs):
        super(Formulario_SeguimientoForm, self).__init__(*args, **kwargs)
        self.fields["Formulario_Seguimiento_Plan"].queryset = Plan.objects.all()
        self.fields["Formulario_Seguimiento"].queryset = Formulario.objects.all()



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

