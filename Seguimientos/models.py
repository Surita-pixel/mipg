from django.db import models
from django.urls import reverse


class Seguimiento(models.Model):

    # Relationships
    seguimiento_formulario = models.OneToOneField("Formularios.Formulario", on_delete=models.CASCADE)
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
