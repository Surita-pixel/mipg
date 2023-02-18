from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class RespuestaListView(generic.ListView):
    model = models.Respuesta
    form_class = forms.RespuestaForm


class RespuestaCreateView(generic.CreateView):
    model = models.Respuesta
    form_class = forms.RespuestaForm


class RespuestaDetailView(generic.DetailView):
    model = models.Respuesta
    form_class = forms.RespuestaForm


class RespuestaUpdateView(generic.UpdateView):
    model = models.Respuesta
    form_class = forms.RespuestaForm
    pk_url_kwarg = "pk"


class RespuestaDeleteView(generic.DeleteView):
    model = models.Respuesta
    success_url = reverse_lazy("Formularios_Respuesta_list")


class PreguntaListView(generic.ListView):
    model = models.Pregunta
    form_class = forms.PreguntaForm


class PreguntaCreateView(generic.CreateView):
    model = models.Pregunta
    form_class = forms.PreguntaForm


class PreguntaDetailView(generic.DetailView):
    model = models.Pregunta
    form_class = forms.PreguntaForm


class PreguntaUpdateView(generic.UpdateView):
    model = models.Pregunta
    form_class = forms.PreguntaForm
    pk_url_kwarg = "pk"


class PreguntaDeleteView(generic.DeleteView):
    model = models.Pregunta
    success_url = reverse_lazy("Formularios_Pregunta_list")


class FormularioListView(generic.ListView):
    model = models.Formulario
    form_class = forms.FormularioForm


class FormularioCreateView(generic.CreateView):
    model = models.Formulario
    form_class = forms.FormularioForm


class FormularioDetailView(generic.DetailView):
    model = models.Formulario
    form_class = forms.FormularioForm


class FormularioUpdateView(generic.UpdateView):
    model = models.Formulario
    form_class = forms.FormularioForm
    pk_url_kwarg = "pk"


class FormularioDeleteView(generic.DeleteView):
    model = models.Formulario
    success_url = reverse_lazy("Formularios_Formulario_list")
