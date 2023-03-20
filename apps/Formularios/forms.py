from django import forms
from apps.Formularios.models import Pregunta
from apps.Formularios.models import Formulario
from . import models


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = models.Respuesta
        fields = [
            "respuesta",
            "pregunta",
        ]

    def __init__(self, *args, **kwargs):
        super(RespuestaForm, self).__init__(*args, **kwargs)
        self.fields["pregunta"].queryset = Pregunta.objects.all()



class PreguntaForm(forms.ModelForm):
    class Meta:
        model = models.Pregunta
        fields = [
            "pregunta",
            "formulario",
        ]

    def __init__(self, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)
        self.fields["formulario"].queryset = Formulario.objects.all()



class FormularioForm(forms.ModelForm):
    class Meta:
        model = models.Formulario
        fields = [
            "nombre",
        ]
