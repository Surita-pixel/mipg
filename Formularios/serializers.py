from rest_framework import serializers

from . import models


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pregunta
        fields = '__all__'

class RespuestaSerializer(serializers.ModelSerializer):
    Pregunta= PreguntaSerializer
    class Meta:
        model = models.Respuesta
        fields = '__all__'

class FormularioSerializer(serializers.ModelSerializer):
    respuestas_formulario = RespuestaSerializer
    preguntas_formulario = PreguntaSerializer

    class Meta:
        model = models.Formulario
        fields = '__all__'
    
    def create(self, validated_data):
        preguntas_data = validated_data.pop('preguntas_formulario')
        respuestas_data = validated_data.pop('respuestas_formulario')
        formulario = models.Formulario.objects.create(**validated_data)
        for pregunta_data in preguntas_data:
            pregunta = models.Pregunta.objects.create(formulario=formulario, **pregunta_data)
        for respuesta_data in respuestas_data:
            respuesta = models.Respuesta.objects.create(formulario=formulario, **respuesta_data)
        return formulario