from django import forms
from . import models


class PlanDeDesarrolloForm(forms.ModelForm):
    class Meta:
        model = models.PlanDeDesarrollo
        fields = [
            "vigencia_fin",
            "meta_nombre",
            "fecha_inicio",
            "vigencia_inicio",
            "indicador_nombre",
            "creado_por",
        ]


class InformeForm(forms.ModelForm):
    class Meta:
        model = models.Informe
        fields = [
            "periodo_reportado",
            "año",
            "plan",
        ]


class PlanForm(forms.ModelForm):
    class Meta:
        model = models.Plan
        fields = [
            "nombre",
            "creado_por",
            "proyecto",
        ]


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields = [
            "codigo",
            "nombre",
            "logro_de_ciudad",
            "objetivo_general",
            "Proposito",
            "plan_de_desarrollo",
            "creado_por",
        ]


class CampoForm(forms.ModelForm):
    class Meta:
        model = models.Campo
        fields = [
            "nombre",
            "meta",
            "indicador",
            "plan",
        ]


class evidenciaForm(forms.ModelForm):
    class Meta:
        model = models.evidencia
        fields = [
            "evidencia",
            "campo",
            "informe",
        ]
