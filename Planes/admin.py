from django.contrib import admin
from django import forms

from . import models

from .forms import TipoPlanChoiceField

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


class TipoPlanAdminForm(forms.ModelForm):
    class Meta:
        model = models.TipoPlan
        fields = "__all__"

class TipoPlanAdmin(admin.ModelAdmin):
    form = TipoPlanAdminForm
    list_display = [
        "nombre_tipo_plan",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


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




class PlanProcesoAdminForm(forms.ModelForm):
    tipo_plan = TipoPlanChoiceField(queryset=models.TipoPlan.objects.all())
    tipo_plan_especifico = forms.ModelChoiceField(queryset=models.TipoPlanEspecifico.objects.none())


    class Meta:
        model = models.PlanProceso
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:
            tipo_plan_id = kwargs['instance'].tipo_plan_id
            if tipo_plan_id:
                tipo_plan = models.TipoPlan.objects.get(id=tipo_plan_id)
                self.fields['tipo_plan_especifico'].queryset = tipo_plan.planes_especificos.all()


class PlanProcesoAdmin(admin.ModelAdmin):
    form = PlanProcesoAdminForm
    list_display = [
        "nombre_plan_proceso",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class PlanAdminForm(forms.ModelForm):

    class Meta:
        model = models.Plan
        fields = "__all__"


class PlanAdmin(admin.ModelAdmin):
    form = PlanAdminForm
    list_display = [
        "plan",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class PlanDesarrolloAdminForm(forms.ModelForm):
    class Meta:
        model = models.PlanDesarrollo
        fields = "__all__"


class PlanDesarrolloAdmin(admin.ModelAdmin):
    form = PlanDesarrolloAdminForm
    list_display = [
        "plan_desarrollo",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]

class TipoPlanEspecificoInline(admin.TabularInline):
    model = models.TipoPlan.planes_especificos.through

class TipoPlanEspecificoAdminForm(forms.ModelForm):

    class Meta:
        model = models.TipoPlanEspecifico
        fields = "__all__"


class TipoPlanEspecificoAdmin(admin.ModelAdmin):
    form = TipoPlanEspecificoAdminForm
    list_display = [
        "nombre_plan_especifico",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.PlanEstrategico, PlanEstrategicoAdmin)
admin.site.register(models.TipoPlan, TipoPlanAdmin)
admin.site.register(models.PlanInversion, PlanInversionAdmin)
admin.site.register(models.PlanProceso, PlanProcesoAdmin)
admin.site.register(models.Plan, PlanAdmin)
admin.site.register(models.PlanDesarrollo, PlanDesarrolloAdmin)
admin.site.register(models.TipoPlanEspecifico, TipoPlanEspecificoAdmin)
