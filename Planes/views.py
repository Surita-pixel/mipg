from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms

# class Home
class UserView(generic.TemplateView):
    template_name = "userview.html"

class PlanEstrategicoListView(generic.ListView):
    model = models.PlanEstrategico
    form_class = forms.PlanEstrategicoForm


class PlanEstrategicoCreateView(generic.CreateView):
    model = models.PlanEstrategico
    form_class = forms.PlanEstrategicoForm


class PlanEstrategicoDetailView(generic.DetailView):
    model = models.PlanEstrategico
    form_class = forms.PlanEstrategicoForm


class PlanEstrategicoUpdateView(generic.UpdateView):
    model = models.PlanEstrategico
    form_class = forms.PlanEstrategicoForm
    pk_url_kwarg = "pk"


class PlanEstrategicoDeleteView(generic.DeleteView):
    model = models.PlanEstrategico
    success_url = reverse_lazy("Planes_PlanEstrategico_list")


class TipoPlanListView(generic.ListView):
    model = models.TipoPlan
    form_class = forms.TipoPlanForm


class TipoPlanCreateView(generic.CreateView):
    model = models.TipoPlan
    form_class = forms.TipoPlanForm


class TipoPlanDetailView(generic.DetailView):
    model = models.TipoPlan
    form_class = forms.TipoPlanForm


class TipoPlanUpdateView(generic.UpdateView):
    model = models.TipoPlan
    form_class = forms.TipoPlanForm
    pk_url_kwarg = "pk"


class TipoPlanDeleteView(generic.DeleteView):
    model = models.TipoPlan
    success_url = reverse_lazy("Planes_TipoPlan_list")


class PlanInversionListView(generic.ListView):
    model = models.PlanInversion
    form_class = forms.PlanInversionForm


class PlanInversionCreateView(generic.CreateView):
    model = models.PlanInversion
    form_class = forms.PlanInversionForm


class PlanInversionDetailView(generic.DetailView):
    model = models.PlanInversion
    form_class = forms.PlanInversionForm


class PlanInversionUpdateView(generic.UpdateView):
    model = models.PlanInversion
    form_class = forms.PlanInversionForm
    pk_url_kwarg = "pk"


class PlanInversionDeleteView(generic.DeleteView):
    model = models.PlanInversion
    success_url = reverse_lazy("Planes_PlanInversion_list")


class PlanProcesoListView(generic.ListView):
    model = models.PlanProceso
    form_class = forms.PlanProcesoForm


class PlanProcesoCreateView(generic.CreateView):
    model = models.PlanProceso
    form_class = forms.PlanProcesoForm


class PlanProcesoDetailView(generic.DetailView):
    model = models.PlanProceso
    form_class = forms.PlanProcesoForm


class PlanProcesoUpdateView(generic.UpdateView):
    model = models.PlanProceso
    form_class = forms.PlanProcesoForm
    pk_url_kwarg = "pk"


class PlanProcesoDeleteView(generic.DeleteView):
    model = models.PlanProceso
    success_url = reverse_lazy("Planes_PlanProceso_list")


class PlanListView(generic.ListView):
    model = models.Plan
    form_class = forms.PlanForm


class PlanCreateView(generic.CreateView):
    model = models.Plan
    form_class = forms.PlanForm
    template_name = "formulacion-planes.html"


class PlanDetailView(generic.DetailView):
    model = models.Plan
    form_class = forms.PlanForm


class PlanUpdateView(generic.UpdateView):
    model = models.Plan
    form_class = forms.PlanForm
    pk_url_kwarg = "pk"


class PlanDeleteView(generic.DeleteView):
    model = models.Plan
    success_url = reverse_lazy("Planes_Plan_list")


class PlanDesarrolloListView(generic.ListView):
    model = models.PlanDesarrollo
    form_class = forms.PlanDesarrolloForm


class PlanDesarrolloCreateView(generic.CreateView):
    model = models.PlanDesarrollo
    form_class = forms.PlanDesarrolloForm


class PlanDesarrolloDetailView(generic.DetailView):
    model = models.PlanDesarrollo
    form_class = forms.PlanDesarrolloForm


class PlanDesarrolloUpdateView(generic.UpdateView):
    model = models.PlanDesarrollo
    form_class = forms.PlanDesarrolloForm
    pk_url_kwarg = "pk"


class PlanDesarrolloDeleteView(generic.DeleteView):
    model = models.PlanDesarrollo
    success_url = reverse_lazy("Planes_PlanDesarrollo_list")


class TipoPlanEspecificoListView(generic.ListView):
    model = models.TipoPlanEspecifico
    form_class = forms.TipoPlanEspecificoForm


class TipoPlanEspecificoCreateView(generic.CreateView):
    model = models.TipoPlanEspecifico
    form_class = forms.TipoPlanEspecificoForm


class TipoPlanEspecificoDetailView(generic.DetailView):
    model = models.TipoPlanEspecifico
    form_class = forms.TipoPlanEspecificoForm


class TipoPlanEspecificoUpdateView(generic.UpdateView):
    model = models.TipoPlanEspecifico
    form_class = forms.TipoPlanEspecificoForm
    pk_url_kwarg = "pk"


class TipoPlanEspecificoDeleteView(generic.DeleteView):
    model = models.TipoPlanEspecifico
    success_url = reverse_lazy("Planes_TipoPlanEspecifico_list")
