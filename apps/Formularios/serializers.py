from rest_framework import serializers

from . import models


class RespuestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Respuesta
        fields = [
            "created",
            "respuesta",
            "last_update",
            "pregunta",
        ]

class PreguntaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pregunta
        fields = [
            "pregunta",
            "created",
            "last_update",
            "formulario",
        ]

class FormularioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Formulario
        fields = [
            "created",
            "last_update",
            "nombre",
        ]
