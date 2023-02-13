from django import forms
from Formularios.models import Respuesta
from Formularios.models import Pregunta
from . import models


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = models.Respuesta
        fields = [
            "respuesta",
        ]


class FormularioForm(forms.ModelForm):
    
    class Meta:
        model = models.Formulario
        fields = [
            "nombre"
        ]

    def __init__(self, *args, **kwargs):
        super(FormularioForm, self).__init__(*args, **kwargs)
        self.fields["respuestas_formulario"].queryset = Respuesta.objects.all()
        self.fields["preguntas_formulario"].queryset = Pregunta.objects.all()



class PreguntaForm(forms.ModelForm):
    class Meta:
        model = models.Pregunta
        fields = [
            "pregunta",
        ]
