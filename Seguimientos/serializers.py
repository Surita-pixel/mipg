from rest_framework import serializers

from . import models
from Formularios.serializers import FormularioSerializer, RespuestaSerializer, PreguntaSerializer
from Departamentos.serializers import OficinaSerializer, PlanSerializer

class Formulario_SeguimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Formulario_Seguimiento
        fields = [
            "last_updated",
            "created",
            "seguimiento_name",
            "Formulario_Seguimiento_Plan",
            "Formulario_Seguimiento",
        ]

class SeguimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Seguimiento
        fields = [
            "last_updated",
            "created",
            "seguimiento_formulario_pivot",
            "oficina",
        ]
