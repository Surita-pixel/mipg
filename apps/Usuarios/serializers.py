from rest_framework import serializers
from . import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = [
            "usuario",
            "nombres",
            "apellidos",
            "username",
            "correo",
            "dependencia",
            "is_superuser",
            "activo",
            "password",
        ]

class UsuarioActivoForm(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = [
            "ID_USUARIO",
            "ES_ACTIVO",
        ]

class UsuarioRolForm(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario_Rol
        fields = [
            "ID_USUARIO",
            "ID_ROL",
        ]

