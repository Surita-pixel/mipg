from rest_framework import viewsets, permissions

from . import serializers
from . import models


class RespuestaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Respuesta class"""

    queryset = models.Respuesta.objects.all()
    serializer_class = serializers.RespuestaSerializer
    permission_classes = [permissions.IsAuthenticated]


class PreguntaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Pregunta class"""

    queryset = models.Pregunta.objects.all()
    serializer_class = serializers.PreguntaSerializer
    permission_classes = [permissions.IsAuthenticated]


class FormularioViewSet(viewsets.ModelViewSet):
    """ViewSet for the Formulario class"""

    queryset = models.Formulario.objects.all()
    serializer_class = serializers.FormularioSerializer
    permission_classes = [permissions.IsAuthenticated]
