from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class SeguimientoListView(generic.ListView):
    model = models.Seguimiento
    form_class = forms.SeguimientoForm


class SeguimientoCreateView(generic.CreateView):
    model = models.Seguimiento
    form_class = forms.SeguimientoForm


class SeguimientoDetailView(generic.DetailView):
    model = models.Seguimiento
    form_class = forms.SeguimientoForm


class SeguimientoUpdateView(generic.UpdateView):
    model = models.Seguimiento
    form_class = forms.SeguimientoForm
    pk_url_kwarg = "pk"


class SeguimientoDeleteView(generic.DeleteView):
    model = models.Seguimiento
    success_url = reverse_lazy("Seguimientos_Seguimiento_list")
