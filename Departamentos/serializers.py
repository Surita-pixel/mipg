from rest_framework import serializers

from . import models


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Plan
        fields = [
            "nombre_plan",
            "last_updated",
            "created",
            "oficina",
        ]

class OficinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Oficina
        fields = [
            "nombre_oficina",
            "last_updated",
            "created",
        ]
