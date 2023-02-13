from django import forms
from Departamentos.models import Oficina
from . import models


class PlanForm(forms.ModelForm):
    class Meta:
        model = models.Plan
        fields = [
            "nombre_plan",
            "oficina",
        ]

    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        self.fields["oficina"].queryset = Oficina.objects.all()



class OficinaForm(forms.ModelForm):
    class Meta:
        model = models.Oficina
        fields = [
            "nombre_oficina",
        ]
