from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PlanViewSet(viewsets.ModelViewSet):
    """ViewSet for the Plan class"""

    queryset = models.Plan.objects.all()
    serializer_class = serializers.PlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class OficinaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Oficina class"""

    queryset = models.Oficina.objects.all()
    serializer_class = serializers.OficinaSerializer
    permission_classes = [permissions.IsAuthenticated]
