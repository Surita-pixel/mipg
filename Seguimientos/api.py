from rest_framework import viewsets, permissions

from . import serializers
from . import models


class SeguimientoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Seguimiento class"""

    queryset = models.Seguimiento.objects.all()
    serializer_class = serializers.SeguimientoSerializer
    permission_classes = [permissions.IsAuthenticated]
