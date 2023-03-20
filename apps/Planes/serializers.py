from rest_framework import serializers

from . import models


class PlanEstrategicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanEstrategico
        fields = [
            "last_updated",
            "plan_estrategico",
            "created",
            "seguimiento_plan_estrategico",
            "planes_inversion",
        ]

class TipoPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TipoPlan
        fields = [
            "last_updated",
            "created",
            "nombre_tipo_plan",
            "plan_proceso",
            "planes_especificos",
        ]

class PlanInversionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanInversion
        fields = [
            "last_updated",
            "created",
            "formulario_inversion",
        ]

class PlanProcesoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanProceso
        fields = [
            "created",
            "nombre_plan_proceso",
            "last_updated",
            "planes_de_inversion",
            "seguimiento_proceso",
        ]

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Plan
        fields = [
            "last_updated",
            "created",
            "plan",
            "oficina",
            "planes_desarrollo",
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

class TipoPlanEspecificoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TipoPlanEspecifico
        fields = [
            "last_updated",
            "created",
            "nombre_plan_especifico",
            "planes_proceso",
        ]
