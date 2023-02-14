from django import forms
from Formularios.models import Formulario
from Planes.models import PlanDesarrollo
from Departamentos.models import Oficina
from Formularios.models import Formulario
from Planes.models import PlanEstrategico
from Planes.models import PlanInversion
from Seguimientos.models import Seguimiento
from Seguimientos.models import Seguimiento
from Planes.models import PlanInversion
from . import models


class PlanInversionForm(forms.ModelForm):
    class Meta:
        model = models.PlanInversion
        fields = [
            "formulario_inversion",
        ]

    def __init__(self, *args, **kwargs):
        super(PlanInversionForm, self).__init__(*args, **kwargs)
        self.fields["formulario_inversion"].queryset = Formulario.objects.all()



class PlanForm(forms.ModelForm):
    class Meta:
        model = models.Plan
        fields = [
            "plan",
            "planes_desarrollo",
            "oficina",
        ]

    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        self.fields["planes_desarrollo"].queryset = PlanDesarrollo.objects.all()
        self.fields["oficina"].queryset = Oficina.objects.all()



class PlanDesarrolloForm(forms.ModelForm):
    class Meta:
        model = models.PlanDesarrollo
        fields = [
            "plan_desarrollo",
            "formulario_plan_desarrollo",
            "planes_estrategicos",
        ]

    def __init__(self, *args, **kwargs):
        super(PlanDesarrolloForm, self).__init__(*args, **kwargs)
        self.fields["formulario_plan_desarrollo"].queryset = Formulario.objects.all()
        self.fields["planes_estrategicos"].queryset = PlanEstrategico.objects.all()



class PlanEstrategicoForm(forms.ModelForm):
    class Meta:
        model = models.PlanEstrategico
        fields = [
            "plan_estrategico",
            "planes_inversion",
            "seguimiento_plan_estrategico",
        ]

    def __init__(self, *args, **kwargs):
        super(PlanEstrategicoForm, self).__init__(*args, **kwargs)
        self.fields["planes_inversion"].queryset = PlanInversion.objects.all()
        self.fields["seguimiento_plan_estrategico"].queryset = Seguimiento.objects.all()



class PlanProcesoForm(forms.ModelForm):
    class Meta:
        model = models.PlanProceso
        fields = [
            "plan_proceso",
            "seguimiento_proceso",
            "planes_de_inversion",
        ]

    def __init__(self, *args, **kwargs):
        super(PlanProcesoForm, self).__init__(*args, **kwargs)
        self.fields["seguimiento_proceso"].queryset = Seguimiento.objects.all()
        self.fields["planes_de_inversion"].queryset = PlanInversion.objects.all()

