from django.contrib import admin
from django import forms

from . import models


class RespuestaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Respuesta
        fields = "__all__"


class RespuestaAdmin(admin.ModelAdmin):
    form = RespuestaAdminForm
    list_display = [
        "last_updated",
        "created",
        "respuesta",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "respuesta",
    ]


class FormularioAdminForm(forms.ModelForm):

    class Meta:
        model = models.Formulario
        fields = "__all__"


class FormularioAdmin(admin.ModelAdmin):
    form = FormularioAdminForm
    list_display = [
        "nombre",
    ]
    readonly_fields = [
        "nombre",
    ]


class PreguntaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Pregunta
        fields = "__all__"


class PreguntaAdmin(admin.ModelAdmin):
    form = PreguntaAdminForm
    list_display = [
        "pregunta",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "pregunta",
        "last_updated",
        "created",
    ]


admin.site.register(models.Respuesta, RespuestaAdmin)
admin.site.register(models.Formulario, FormularioAdmin)
admin.site.register(models.Pregunta, PreguntaAdmin)
