from django.contrib import admin
from django import forms

from . import models


class PlanDeDesarrolloAdminForm(forms.ModelForm):

    class Meta:
        model = models.PlanDeDesarrollo
        fields = "__all__"


class PlanDeDesarrolloAdmin(admin.ModelAdmin):
    form = PlanDeDesarrolloAdminForm
    list_display = [
        "nombre",
        "vigencia_inicio",
        "vigencia_fin",
        "meta_nombre",
        "fecha_inicio",
        "ultima_actualizacion",
        "indicador_nombre",
    ]



class InformeAdminForm(forms.ModelForm):

    class Meta:
        model = models.Informe
        fields = "__all__"


class InformeAdmin(admin.ModelAdmin):
    form = InformeAdminForm
    list_display = [
        "periodo_reportado",
        "creado_por",
        "ultima_actualizacion",
        "año",
    ]



class PlanAdminForm(forms.ModelForm):

    class Meta:
        model = models.Plan
        fields = "__all__"


class PlanAdmin(admin.ModelAdmin):
    form = PlanAdminForm
    list_display = [
        "nombre",
        "ultima_actualizacion",
        "fecha_creacion",
    ]


class ProyectoAdminForm(forms.ModelForm):

    class Meta:
        model = models.Proyecto
        fields = "__all__"


class ProyectoAdmin(admin.ModelAdmin):
    form = ProyectoAdminForm
    list_display = [
        "codigo",
        "nombre",
        "logro_de_ciudad",
        "creado",
        "ultima_actualizacion",
        "objetivo_general",
        "Proposito",
    ]


class CampoAdminForm(forms.ModelForm):

    class Meta:
        model = models.Campo
        fields = "__all__"


class CampoAdmin(admin.ModelAdmin):
    form = CampoAdminForm
    list_display = [
        "nombre",
        "created",
        "meta",
        "indicador",
        "last_updated",
    ]


class evidenciaAdminForm(forms.ModelForm):

    class Meta:
        model = models.evidencia
        fields = "__all__"


class evidenciaAdmin(admin.ModelAdmin):
    form = evidenciaAdminForm
    list_display = [
        "campo",
        "informe",
        "evidencia",
        "ultima_actualizacion",
        "creado_por",
    ]



admin.site.register(models.PlanDeDesarrollo, PlanDeDesarrolloAdmin)
admin.site.register(models.Informe, InformeAdmin)
admin.site.register(models.Plan, PlanAdmin)
admin.site.register(models.Proyecto, ProyectoAdmin)
admin.site.register(models.Campo, CampoAdmin)
admin.site.register(models.evidencia, evidenciaAdmin)
