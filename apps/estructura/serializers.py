from rest_framework import serializers

from . import models


class PlanDeDesarrolloSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanDeDesarrollo
        fields = [
            "vigencia_fin",
            "meta_nombre",
            "fecha_inicio",
            "vigencia_inicio",
            "ultima_actualizacion",
            "indicador_nombre",
        ]

class InformeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Informe
        fields = [
            "periodo_reportado",
            "creado_por",
            "ultima_actualizacion",
            "año",
        ]

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Plan
        fields = [
            "ultima_actualizacion",
            "nombre",
            "fecha_creacion",
        ]

class ProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Proyecto
        fields = [
            "codigo",
            "nombre",
            "logro_de_ciudad",
            "creado",
            "ultima_actualizacion",
            "objetivo_general",
            "Proposito",
        ]

class CampoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Campo
        fields = [
            "nombre",
            "created",
            "meta",
            "indicador",
            "last_updated",
        ]

class evidenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.evidencia
        fields = [
            "ultima_actualizacion",
            "creado_por",
            "evidencia",
        ]
