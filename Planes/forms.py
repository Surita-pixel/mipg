from django import forms
from django.contrib.admin import widgets
from Seguimientos.models import Seguimiento
from Planes.models import PlanInversion, PlanProceso, TipoPlanEspecifico, TipoPlan
from Formularios.models import Formulario
from Planes.models import PlanInversion
from Seguimientos.models import Seguimiento
from Departamentos.models import Oficina
from Planes.models import PlanDesarrollo
from Formularios.models import Formulario
from Planes.models import PlanEstrategico
from Planes.models import PlanProceso
from . import models

class TipoPlanChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre_tipo_plan

class PlanEstrategicoForm(forms.ModelForm):
    class Meta:
        model = models.PlanEstrategico
        fields = [
            "plan_estrategico",
            "seguimiento_plan_estrategico",
            "planes_inversion",
        ]

    def __init__(self, *args, **kwargs):
        super(PlanEstrategicoForm, self).__init__(*args, **kwargs)
        self.fields["seguimiento_plan_estrategico"].queryset = Seguimiento.objects.all()
        self.fields["planes_inversion"].queryset = PlanInversion.objects.all()


tipoplan_nombre = (
    ("PGC", "PLAN DE GESTION CIUDADANA"),
    ("PGA", "PLANES DE GESTION AMBIENTAL"),
    ("PGIT", "PLAN DE GESTION DE INFORMACION Y LA TECNOLOGIA"),
    ("PET", "PLAN ESTRATEGICO DE TALENTO HUMANO"),
    ("PGSSA", "PLAN DE GESTION DE SEGURIDAD Y SALUD AMBIENTAL"),
)

class TipoPlanForm(forms.ModelForm):
    nombre = forms.ChoiceField(choices=tipoplan_nombre)
    sub_categoria = forms.ModelChoiceField(queryset=TipoPlanEspecifico.objects.filter(filtro__isnull=False))
    
    class Meta:
        model = models.TipoPlan
        fields = [
            "nombre",
            "sub_categoria"
        ]

class PlanInversionForm(forms.ModelForm):
    class Meta:
        model = models.PlanInversion
        fields = [
            "formulario_inversion",
        ]

    def __init__(self, *args, **kwargs):
        super(PlanInversionForm, self).__init__(*args, **kwargs)
        self.fields["formulario_inversion"].queryset = Formulario.objects.all()



class PlanProcesoForm(forms.ModelForm):
    tipo_plan = forms.ModelChoiceField(queryset=TipoPlan.objects.all(), empty_label="selecciona un tipo de plan")
    class Meta:
        model = models.PlanProceso
        fields = [
            "nombre_plan_proceso",
            "tipo_plan",
            "seguimiento_proceso",
            "planes_de_inversion"
        ]
        

    def __init__(self, *args, **kwargs):
        super(PlanProcesoForm, self).__init__(*args, **kwargs)
        self.fields["planes_de_inversion"].queryset = PlanInversion.objects.all()
        self.fields["seguimiento_proceso"].queryset = Seguimiento.objects.all()



class PlanForm(forms.ModelForm):
    areas_responsables = forms.ModelChoiceField(queryset=Oficina.objects.all(),
                                          widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkboxes', 'required': True}),
                                          to_field_name="nombre_oficina")
    plan_desarrollo = forms.ModelChoiceField(queryset=models.PlanDesarrollo.objects.all(), label="plan desarrollo",
                                             widget=forms.Select(attrs={'class': 'select w-select', 'id':"Nombre-del-plan", 'required': True}))
    tipo_de_plan = forms.ModelChoiceField(queryset=models.TipoPlan.objects.filter(filtro__isnull=True),
                                          widget=forms.Select(attrs={'class': 'select w-select', 'required': True}))

    tipo_de_plan_especifico = forms.ModelChoiceField(queryset=models.TipoPlanEspecifico.objects.filter(filtro__isnull=False),
                                                     widget=forms.Select(attrs={'class': 'select w-select', 'required': True}))

    class Meta:
        model = models.Plan
        fields = [
            "plan",
            'fecha_inicio',
            'fecha_final',
            'otros_campos',
        ]
        widgets = {
            # 'plan': forms.CharField(required=True),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'fecha_final': forms.DateInput(attrs={'type': 'date', 'required': True}),
        }



class PlanDesarrolloForm(forms.ModelForm):
    class Meta:
        model = models.PlanDesarrollo
        fields = [
            "plan_desarrollo",
            "planes_estrategicos",
        ]

    def __init__(self, *args, **kwargs):
        super(PlanDesarrolloForm, self).__init__(*args, **kwargs)
        self.fields["formulario_plan_desarrollo"].queryset = Formulario.objects.all()
        self.fields["planes_estrategicos"].queryset = PlanEstrategico.objects.all()



class TipoPlanEspecificoForm(forms.ModelForm):
    class Meta:
        model = models.TipoPlanEspecifico
        fields = [
            "nombre",
            "filtro"
        ]


