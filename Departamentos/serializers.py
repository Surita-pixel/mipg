from rest_framework import serializers

from . import models


class OficinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Oficina
        fields = [
            "last_updated",
            "nombre_oficina",
            "created",
        ]
