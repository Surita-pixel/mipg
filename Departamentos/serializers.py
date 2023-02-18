from rest_framework import serializers

from . import models


class OficinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Oficina
        fields = [
            "nombre_oficina",
            "last_updated",
            "created",
        ]
