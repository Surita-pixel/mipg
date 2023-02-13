from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


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
    success_url = reverse_lazy("Departamentos_Plan_list")


class OficinaListView(generic.ListView):
    model = models.Oficina
    form_class = forms.OficinaForm


class OficinaCreateView(generic.CreateView):
    model = models.Oficina
    form_class = forms.OficinaForm


class OficinaDetailView(generic.DetailView):
    model = models.Oficina
    form_class = forms.OficinaForm


class OficinaUpdateView(generic.UpdateView):
    model = models.Oficina
    form_class = forms.OficinaForm
    pk_url_kwarg = "pk"


class OficinaDeleteView(generic.DeleteView):
    model = models.Oficina
    success_url = reverse_lazy("Departamentos_Oficina_list")
