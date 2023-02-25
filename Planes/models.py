from django import forms
from django.db import models
from django.urls import reverse


class PlanEstrategico(models.Model):

    # Relationships
    seguimiento_plan_estrategico = models.ForeignKey("Seguimientos.Seguimiento", on_delete=models.CASCADE, blank=True)
    planes_inversion = models.ForeignKey("Planes.PlanInversion", on_delete=models.CASCADE, blank=True)

    # Fields
    plan_estrategico = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Planes_PlanEstrategico_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Planes_PlanEstrategico_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Planes_PlanEstrategico_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Planes_PlanEstrategico_htmx_delete", args=(self.pk,))


# class TipoPlanBase(models.Model):
#     nombre = models.TextField(max_length=200)
#     filtro = models.CharField(max_length=50, blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True, editable=False)
#     last_updated = models.DateTimeField(auto_now=True, editable=False)
#     class Meta:
#         db_table = "Plan_TipoPlan"
#         abstract = True


class TipoPlan(models.Model):
    nombre = models.TextField(max_length=200)
    plan_proceso = models.ForeignKey("Planes.PlanProceso", on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = "tipo_plan"
        managed = False
    def __str__(self):
        return str(self.nombre)

    def get_absolute_url(self):
        return reverse("Planes_TipoPlan_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Planes_TipoPlan_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Planes_TipoPlan_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Planes_TipoPlan_htmx_delete", args=(self.pk,))
    

class TipoPlanEspecifico(models.Model):
    nombre = models.TextField(max_length=200)
    filtro = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = "tipo_plan"
        managed = False

    def __str__(self):
        return str(self.nombre)

    def get_absolute_url(self):
        return reverse("Planes_TipoPlanEspecifico_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Planes_TipoPlanEspecifico_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Planes_TipoPlanEspecifico_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Planes_TipoPlanEspecifico_htmx_delete", args=(self.pk,))


class PlanInversion(models.Model):

    # Relationships
    formulario_inversion = models.ForeignKey("Formularios.Formulario", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Planes_PlanInversion_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Planes_PlanInversion_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Planes_PlanInversion_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Planes_PlanInversion_htmx_delete", args=(self.pk,))


class PlanProceso(models.Model):

    # Fields
    nombre_plan_proceso = models.TextField(max_length=100)
    # Relationships
    planes_de_inversion = models.ForeignKey("Planes.PlanInversion", on_delete=models.CASCADE, blank=True, null=True)
    seguimiento_proceso = models.ForeignKey("Seguimientos.Seguimiento", on_delete=models.CASCADE, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.nombre_plan_proceso)

    def get_absolute_url(self):
        return reverse("Planes_PlanProceso_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Planes_PlanProceso_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Planes_PlanProceso_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Planes_PlanProceso_htmx_delete", args=(self.pk,))


class Plan(models.Model):

    # Fields
    plan = models.TextField(max_length=100)
    # Relationships
    oficina = models.ForeignKey("Departamentos.Oficina", on_delete=models.CASCADE)
    planes_desarrollo = models.ForeignKey("Planes.PlanDesarrollo", on_delete=models.CASCADE, blank=True)

    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Planes_Plan_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Planes_Plan_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Planes_Plan_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Planes_Plan_htmx_delete", args=(self.pk,))


class PlanDesarrollo(models.Model):

    # Fields
    plan_desarrollo = models.TextField(max_length=100)
    # Relationships
    formulario_plan_desarrollo = models.ForeignKey("Formularios.Formulario", on_delete=models.CASCADE)
    planes_estrategicos = models.ForeignKey("Planes.PlanEstrategico", on_delete=models.CASCADE, blank=True)

    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Planes_PlanDesarrollo_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Planes_PlanDesarrollo_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Planes_PlanDesarrollo_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Planes_PlanDesarrollo_htmx_delete", args=(self.pk,))



