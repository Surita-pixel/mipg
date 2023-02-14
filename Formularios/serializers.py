from rest_framework import serializers

from . import models


class RespuestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Respuesta
        fields = [
            "last_update",
            "created",
            "respuesta",
            "pregunta",
        ]

class FormularioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Formulario
        fields = [
            "nombre",
            "last_update",
            "created",
        ]

class PreguntaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pregunta
        fields = [
            "created",
            "last_update",
            "pregunta",
            "formulario",
        ]
