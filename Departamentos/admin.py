from django.contrib import admin
from django import forms

from . import models


class OficinaAdminForm(forms.ModelForm):

    class Meta:
        model = models.Oficina
        fields = "__all__"


class OficinaAdmin(admin.ModelAdmin):
    form = OficinaAdminForm
    list_display = [
        "last_updated",
        "nombre_oficina",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "nombre_oficina",
        "created",
    ]


admin.site.register(models.Oficina, OficinaAdmin)
