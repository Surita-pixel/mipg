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
        "created",
        "respuesta",
        "last_update",
    ]
    readonly_fields = [
        "created",
        "last_update",
    ]
class RespuestasInLine(admin.TabularInline):
    model = models.Respuesta


class PreguntaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Pregunta
        fields = "__all__"


class PreguntaAdmin(admin.ModelAdmin):
    form = PreguntaAdminForm
    inlines = [RespuestasInLine]
    list_display = [
        "pregunta",
        "created",
        "last_update",
    ]

    readonly_fields = [
        "created",
        "last_update",
    ]

class PreguntaInline(admin.TabularInline):
    model = models.Pregunta
    inlines = [RespuestasInLine]
    show_change_link = True


class FormularioAdminForm(forms.ModelForm):

    class Meta:
        model = models.Formulario
        fields = "__all__"


class FormularioAdmin(admin.ModelAdmin):
    form = FormularioAdminForm
    inlines = [PreguntaInline]
    list_display = [
        "created",
        "last_update",
        "nombre",
    ]
    readonly_fields = [
        "created",
        "last_update",
    ]


admin.site.register(models.Respuesta, RespuestaAdmin)
admin.site.register(models.Pregunta, PreguntaAdmin)
admin.site.register(models.Formulario, FormularioAdmin)
