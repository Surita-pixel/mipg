from django.contrib import admin
from django import forms

from . import models


class SeguimientoAdminForm(forms.ModelForm):

    class Meta:
        model = models.Seguimiento
        fields = "__all__"


class SeguimientoAdmin(admin.ModelAdmin):
    form = SeguimientoAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class Formulario_SeguimientoAdminForm(forms.ModelForm):

    class Meta:
        model = models.Formulario_Seguimiento
        fields = "__all__"


class Formulario_SeguimientoAdmin(admin.ModelAdmin):
    form = Formulario_SeguimientoAdminForm
    list_display = [
        "created",
        "last_updated",
        "formulario_seguimiento",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "formulario_seguimiento",
    ]


admin.site.register(models.Seguimiento, SeguimientoAdmin)
admin.site.register(models.Formulario_Seguimiento, Formulario_SeguimientoAdmin)
