from rest_framework import viewsets, permissions

from . import serializers
from . import models


class UsuarioViewSet(viewsets.ModelViewSet):
    """ViewSet for the Usuario class"""

    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]