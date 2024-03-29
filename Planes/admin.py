from django.contrib import admin
from django import forms

from . import models
from Departamentos.models import Oficina

from .forms import TipoPlanChoiceField, TipoPlanForm, PlanForm

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


class TipoPlanAdminForm(TipoPlanForm):
    pass

class TipoPlanAdmin(admin.ModelAdmin):
    form = TipoPlanAdminForm
    list_display = [
        "nombre",
        "sub_categoria"
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



class PlanAdmin(admin.ModelAdmin):
    form = PlanForm
    list_display = [
        "plan",
        'fecha_inicio',
        'fecha_final',
        'otros_campos',
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


class TipoPlanEspecificoAdminForm(forms.ModelForm):

    class Meta:
        model = models.TipoPlanEspecifico
        fields = ["nombre","filtro"]


class TipoPlanEspecificoAdmin(admin.ModelAdmin):
    form = TipoPlanEspecificoAdminForm
    list_display = [
        "nombre",
        "filtro"
    ]


admin.site.register(models.PlanEstrategico, PlanEstrategicoAdmin)
admin.site.register(models.TipoPlan, TipoPlanAdmin)
admin.site.register(models.PlanInversion, PlanInversionAdmin)
admin.site.register(models.PlanProceso, PlanProcesoAdmin)
admin.site.register(models.Plan, PlanAdmin)
admin.site.register(models.PlanDesarrollo, PlanDesarrolloAdmin)
admin.site.register(models.TipoPlanEspecifico, TipoPlanEspecificoAdmin)
