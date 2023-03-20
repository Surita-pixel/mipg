from django.contrib import admin
from django import forms
from apps.Usuarios.ldap import Ldap
from . import models


class UsuarioAdminForm(forms.ModelForm):
    
    class Meta:
        model = models.Usuario
        fields = "__all__"


class UsuarioAdmin(admin.ModelAdmin):
    form = UsuarioAdminForm

    def get_changeform_initial_data(self, request):
        if ('ldap' in request.GET ):
            ldap = Ldap()
            user_ldap = ldap.search_exact_user(request.GET.get('ldap'))
            if(user_ldap):
                return {
                    'username': user_ldap['usuario'],
                    'nombres': user_ldap['nombre_completo'],
                    'correo': user_ldap['correo'],
                    'email': user_ldap['correo'],
                    'is_active': user_ldap['activo'],
                    'activo': user_ldap['activo'],
                }
        return {}



admin.site.register(models.Usuario, UsuarioAdmin)