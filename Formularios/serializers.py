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

    pregunta =  serializers.StringRelatedField()

    def to_representation(self,instance):
        self.fields['pregunta'] = PreguntaSerializer(read_only=True)
        return super(FormularioSerializer,self).to_representation(instance)  

    class Meta:
        model = models.Formulario
        fields = ['id','nombre', 'pregunta']
        
    
    def create(self, validated_data):
        preguntas_data = validated_data.pop('preguntas_formulario')
        
        custom_data = {
            **validated_data
        }
        formulario = models.Formulario.objects.create(**custom_data)
        for pregunta_data in preguntas_data:
            pregunta = models.Pregunta.objects.create(formulario=formulario, **pregunta_data)
        # for respuesta_data in respuestas_data:
        #     respuesta = models.Respuesta.objects.create(formulario=formulario, **respuesta_data)
        return formulario