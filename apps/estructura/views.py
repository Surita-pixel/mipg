from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class PlanDeDesarrolloListView(generic.ListView):
    model = models.PlanDeDesarrollo
    form_class = forms.PlanDeDesarrolloForm


class PlanDeDesarrolloCreateView(generic.CreateView):
    model = models.PlanDeDesarrollo
    form_class = forms.PlanDeDesarrolloForm


class PlanDeDesarrolloDetailView(generic.DetailView):
    model = models.PlanDeDesarrollo
    form_class = forms.PlanDeDesarrolloForm


class PlanDeDesarrolloUpdateView(generic.UpdateView):
    model = models.PlanDeDesarrollo
    form_class = forms.PlanDeDesarrolloForm
    pk_url_kwarg = "pk"


class PlanDeDesarrolloDeleteView(generic.DeleteView):
    model = models.PlanDeDesarrollo
    success_url = reverse_lazy("estructura_PlanDeDesarrollo_list")


class InformeListView(generic.ListView):
    model = models.Informe
    form_class = forms.InformeForm


class InformeCreateView(generic.CreateView):
    model = models.Informe
    form_class = forms.InformeForm


class InformeDetailView(generic.DetailView):
    model = models.Informe
    form_class = forms.InformeForm


class InformeUpdateView(generic.UpdateView):
    model = models.Informe
    form_class = forms.InformeForm
    pk_url_kwarg = "pk"


class InformeDeleteView(generic.DeleteView):
    model = models.Informe
    success_url = reverse_lazy("estructura_Informe_list")


class PlanListView(generic.ListView):
    model = models.Plan
    form_class = forms.PlanForm


class PlanCreateView(generic.CreateView):
    model = models.Plan
    form_class = forms.PlanForm


class PlanDetailView(generic.DetailView):
    model = models.Plan
    form_class = forms.PlanForm


class PlanUpdateView(generic.UpdateView):
    model = models.Plan
    form_class = forms.PlanForm
    pk_url_kwarg = "pk"


class PlanDeleteView(generic.DeleteView):
    model = models.Plan
    success_url = reverse_lazy("estructura_Plan_list")


class ProyectoListView(generic.ListView):
    model = models.Proyecto
    form_class = forms.ProyectoForm


class ProyectoCreateView(generic.CreateView):
    model = models.Proyecto
    form_class = forms.ProyectoForm


class ProyectoDetailView(generic.DetailView):
    model = models.Proyecto
    form_class = forms.ProyectoForm


class ProyectoUpdateView(generic.UpdateView):
    model = models.Proyecto
    form_class = forms.ProyectoForm
    pk_url_kwarg = "pk"


class ProyectoDeleteView(generic.DeleteView):
    model = models.Proyecto
    success_url = reverse_lazy("estructura_Proyecto_list")


class CampoListView(generic.ListView):
    model = models.Campo
    form_class = forms.CampoForm


class CampoCreateView(generic.CreateView):
    model = models.Campo
    form_class = forms.CampoForm


class CampoDetailView(generic.DetailView):
    model = models.Campo
    form_class = forms.CampoForm


class CampoUpdateView(generic.UpdateView):
    model = models.Campo
    form_class = forms.CampoForm
    pk_url_kwarg = "pk"


class CampoDeleteView(generic.DeleteView):
    model = models.Campo
    success_url = reverse_lazy("estructura_Campo_list")


class evidenciaListView(generic.ListView):
    model = models.evidencia
    form_class = forms.evidenciaForm


class evidenciaCreateView(generic.CreateView):
    model = models.evidencia
    form_class = forms.evidenciaForm


class evidenciaDetailView(generic.DetailView):
    model = models.evidencia
    form_class = forms.evidenciaForm


class evidenciaUpdateView(generic.UpdateView):
    model = models.evidencia
    form_class = forms.evidenciaForm
    pk_url_kwarg = "pk"


class evidenciaDeleteView(generic.DeleteView):
    model = models.evidencia
    success_url = reverse_lazy("estructura_evidencia_list")
