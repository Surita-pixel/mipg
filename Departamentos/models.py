from django.db import models
from django.urls import reverse


class Oficina(models.Model):

    # Fields
    nombre_oficina = models.TextField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Departamentos_Oficina_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Departamentos_Oficina_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Departamentos_Oficina_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Departamentos_Oficina_htmx_delete", args=(self.pk,))
