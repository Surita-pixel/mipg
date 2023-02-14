from rest_framework import serializers

from . import models


class PlanInversionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanInversion
        fields = [
            "last_updated",
            "created",
            "formulario_inversion",
        ]

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Plan
        fields = [
            "last_updated",
            "plan",
            "created",
            "planes_desarrollo",
            "oficina",
        ]

class PlanDesarrolloSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanDesarrollo
        fields = [
            "last_updated",
            "created",
            "plan_desarrollo",
            "formulario_plan_desarrollo",
            "planes_estrategicos",
        ]

class PlanEstrategicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanEstrategico
        fields = [
            "last_updated",
            "plan_estrategico",
            "created",
            "planes_inversion",
            "seguimiento_plan_estrategico",
        ]

class PlanProcesoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanProceso
        fields = [
            "plan_proceso",
            "created",
            "last_updated",
            "seguimiento_proceso",
            "planes_de_inversion",
        ]
