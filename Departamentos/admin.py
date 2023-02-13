from django.contrib import admin
from django import forms

from . import models


class PlanAdminForm(forms.ModelForm):

    class Meta:
        model = models.Plan
        fields = "__all__"


class PlanAdmin(admin.ModelAdmin):
    form = PlanAdminForm
    list_display = [
        "nombre_plan",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "nombre_plan",
        "last_updated",
        "created",
    ]


class OficinaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Oficina
        fields = "__all__"


class OficinaAdmin(admin.ModelAdmin):
    form = OficinaAdminForm
    list_display = [
        "nombre_oficina",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "nombre_oficina",
        "last_updated",
        "created",
    ]


admin.site.register(models.Plan, PlanAdmin)
admin.site.register(models.Oficina, OficinaAdmin)
