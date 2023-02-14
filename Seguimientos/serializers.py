from rest_framework import serializers

from . import models


class SeguimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Seguimiento
        fields = [
            "created",
            "last_updated",
            "seguimiento_formulario_pivot",
            "oficina",
        ]

class Formulario_SeguimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Formulario_Seguimiento
        fields = [
            "created",
            "last_updated",
            "formulario_seguimiento",
            "Formulario_Seguimiento",
            "Formulario_Seguimiento_Plan",
        ]
