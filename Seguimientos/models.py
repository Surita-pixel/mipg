from django.db import models
from django.urls import reverse


class Seguimiento(models.Model):

    # Relationships
    seguimiento_formulario_pivot = models.ForeignKey("Seguimientos.Formulario_Seguimiento", on_delete=models.CASCADE)
    oficina = models.ForeignKey("Departamentos.Oficina", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Seguimientos_Seguimiento_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Seguimientos_Seguimiento_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Seguimientos_Seguimiento_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Seguimientos_Seguimiento_htmx_delete", args=(self.pk,))


class Formulario_Seguimiento(models.Model):

    # Relationships
    Formulario_Seguimiento = models.ForeignKey("Formularios.Formulario", on_delete=models.CASCADE)
    Formulario_Seguimiento_Plan = models.ForeignKey("Planes.Plan", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    formulario_seguimiento = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Seguimientos_Formulario_Seguimiento_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Seguimientos_Formulario_Seguimiento_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Seguimientos_Formulario_Seguimiento_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Seguimientos_Formulario_Seguimiento_htmx_delete", args=(self.pk,))
