from rest_framework import serializers

from . import models


class SeguimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Seguimiento
        fields = [
            "created",
            "last_updated",
            "seguimiento_formulario",
            "oficina",
        ]
