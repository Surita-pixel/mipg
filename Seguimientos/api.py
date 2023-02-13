from rest_framework import viewsets, permissions

from . import serializers
from . import models


class Formulario_SeguimientoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Formulario_Seguimiento class"""

    queryset = models.Formulario_Seguimiento.objects.all()
    serializer_class = serializers.Formulario_SeguimientoSerializer
    permission_classes = [permissions.IsAuthenticated]


class SeguimientoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Seguimiento class"""

    queryset = models.Seguimiento.objects.all()
    serializer_class = serializers.SeguimientoSerializer
    permission_classes = [permissions.IsAuthenticated]
