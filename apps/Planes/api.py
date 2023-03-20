from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PlanEstrategicoViewSet(viewsets.ModelViewSet):
    """ViewSet for the PlanEstrategico class"""

    queryset = models.PlanEstrategico.objects.all()
    serializer_class = serializers.PlanEstrategicoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TipoPlanViewSet(viewsets.ModelViewSet):
    """ViewSet for the TipoPlan class"""

    queryset = models.TipoPlan.objects.all()
    serializer_class = serializers.TipoPlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlanInversionViewSet(viewsets.ModelViewSet):
    """ViewSet for the PlanInversion class"""

    queryset = models.PlanInversion.objects.all()
    serializer_class = serializers.PlanInversionSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlanProcesoViewSet(viewsets.ModelViewSet):
    """ViewSet for the PlanProceso class"""

    queryset = models.PlanProceso.objects.all()
    serializer_class = serializers.PlanProcesoSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlanViewSet(viewsets.ModelViewSet):
    """ViewSet for the Plan class"""

    queryset = models.Plan.objects.all()
    serializer_class = serializers.PlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlanDesarrolloViewSet(viewsets.ModelViewSet):
    """ViewSet for the PlanDesarrollo class"""

    queryset = models.PlanDesarrollo.objects.all()
    serializer_class = serializers.PlanDesarrolloSerializer
    permission_classes = [permissions.IsAuthenticated]


class TipoPlanEspecificoViewSet(viewsets.ModelViewSet):
    """ViewSet for the TipoPlanEspecifico class"""

    queryset = models.TipoPlanEspecifico.objects.all()
    serializer_class = serializers.TipoPlanEspecificoSerializer
    permission_classes = [permissions.IsAuthenticated]
