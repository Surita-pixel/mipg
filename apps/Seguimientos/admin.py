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


admin.site.register(models.Seguimiento, SeguimientoAdmin)
