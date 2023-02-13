from django.views import generic
from django.urls import reverse_lazy

from rest_framework import generics

from . import serializers
from . import models
from . import forms


class PreguntaListAPIView(generics.ListAPIView):
    serializer_class = serializers.PreguntaSerializer
    def get_queryset(self):
        return models.Pregunta.objects.all()

class PreguntaCreateView(generics.CreateAPIView):
    serializer_class = serializers.PreguntaSerializer


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


class RespuestaListView(generic.ListView):
    model = models.Respuesta
    form_class = forms.RespuestaForm


class RespuestaCreateView(generics.CreateAPIView):
    serializer_class = serializers.RespuestaSerializer


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


class FormularioListAPIView(generics.ListAPIView):
    serializer_class = serializers.FormularioSerializer
    def get_queryset(self):
        return models.Formulario.objects.all()


class FormularioCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.FormularioSerializer


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
