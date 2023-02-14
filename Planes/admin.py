from django.contrib import admin
from django import forms

from . import models


class PlanInversionAdminForm(forms.ModelForm):

    class Meta:
        model = models.PlanInversion
        fields = "__all__"


class PlanInversionAdmin(admin.ModelAdmin):
    form = PlanInversionAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class PlanAdminForm(forms.ModelForm):

    class Meta:
        model = models.Plan
        fields = "__all__"


class PlanAdmin(admin.ModelAdmin):
    form = PlanAdminForm
    list_display = [
        "last_updated",
        "plan",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "plan",
        "created",
    ]


class PlanDesarrolloAdminForm(forms.ModelForm):

    class Meta:
        model = models.PlanDesarrollo
        fields = "__all__"


class PlanDesarrolloAdmin(admin.ModelAdmin):
    form = PlanDesarrolloAdminForm
    list_display = [
        "last_updated",
        "created",
        "plan_desarrollo",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "plan_desarrollo",
    ]


class PlanEstrategicoAdminForm(forms.ModelForm):

    class Meta:
        model = models.PlanEstrategico
        fields = "__all__"


class PlanEstrategicoAdmin(admin.ModelAdmin):
    form = PlanEstrategicoAdminForm
    list_display = [
        "last_updated",
        "plan_estrategico",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "plan_estrategico",
        "created",
    ]


class PlanProcesoAdminForm(forms.ModelForm):

    class Meta:
        model = models.PlanProceso
        fields = "__all__"


class PlanProcesoAdmin(admin.ModelAdmin):
    form = PlanProcesoAdminForm
    list_display = [
        "plan_proceso",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "plan_proceso",
        "created",
        "last_updated",
    ]


admin.site.register(models.PlanInversion, PlanInversionAdmin)
admin.site.register(models.Plan, PlanAdmin)
admin.site.register(models.PlanDesarrollo, PlanDesarrolloAdmin)
admin.site.register(models.PlanEstrategico, PlanEstrategicoAdmin)
admin.site.register(models.PlanProceso, PlanProcesoAdmin)
