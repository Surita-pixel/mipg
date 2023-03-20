from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PlanDeDesarrolloViewSet(viewsets.ModelViewSet):
    """ViewSet for the PlanDeDesarrollo class"""

    queryset = models.PlanDeDesarrollo.objects.all()
    serializer_class = serializers.PlanDeDesarrolloSerializer
    permission_classes = [permissions.IsAuthenticated]


class InformeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Informe class"""

    queryset = models.Informe.objects.all()
    serializer_class = serializers.InformeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlanViewSet(viewsets.ModelViewSet):
    """ViewSet for the Plan class"""

    queryset = models.Plan.objects.all()
    serializer_class = serializers.PlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProyectoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Proyecto class"""

    queryset = models.Proyecto.objects.all()
    serializer_class = serializers.ProyectoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CampoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Campo class"""

    queryset = models.Campo.objects.all()
    serializer_class = serializers.CampoSerializer
    permission_classes = [permissions.IsAuthenticated]


class evidenciaViewSet(viewsets.ModelViewSet):
    """ViewSet for the evidencia class"""

    queryset = models.evidencia.objects.all()
    serializer_class = serializers.evidenciaSerializer
    permission_classes = [permissions.IsAuthenticated]
