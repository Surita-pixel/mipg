from django.contrib import admin
from django import forms

from . import models


class Formulario_SeguimientoAdminForm(forms.ModelForm):

    class Meta:
        model = models.Formulario_Seguimiento
        fields = "__all__"


class Formulario_SeguimientoAdmin(admin.ModelAdmin):
    form = Formulario_SeguimientoAdminForm
    list_display = [
        "last_updated",
        "created",
        "seguimiento_name",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "seguimiento_name",
    ]


class SeguimientoAdminForm(forms.ModelForm):

    class Meta:
        model = models.Seguimiento
        fields = "__all__"


class SeguimientoAdmin(admin.ModelAdmin):
    form = SeguimientoAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.Formulario_Seguimiento, Formulario_SeguimientoAdmin)
admin.site.register(models.Seguimiento, SeguimientoAdmin)
