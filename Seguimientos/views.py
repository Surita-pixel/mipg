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


class Formulario_SeguimientoListView(generic.ListView):
    model = models.Formulario_Seguimiento
    form_class = forms.Formulario_SeguimientoForm


class Formulario_SeguimientoCreateView(generic.CreateView):
    model = models.Formulario_Seguimiento
    form_class = forms.Formulario_SeguimientoForm


class Formulario_SeguimientoDetailView(generic.DetailView):
    model = models.Formulario_Seguimiento
    form_class = forms.Formulario_SeguimientoForm


class Formulario_SeguimientoUpdateView(generic.UpdateView):
    model = models.Formulario_Seguimiento
    form_class = forms.Formulario_SeguimientoForm
    pk_url_kwarg = "pk"


class Formulario_SeguimientoDeleteView(generic.DeleteView):
    model = models.Formulario_Seguimiento
    success_url = reverse_lazy("Seguimientos_Formulario_Seguimiento_list")
