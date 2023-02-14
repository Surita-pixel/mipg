from django.db import models
from django.urls import reverse


class Respuesta(models.Model):

    # Relationships
    pregunta = models.ForeignKey("Formularios.Pregunta", on_delete=models.CASCADE)

    # Fields
    last_update = models.DateTimeField(auto_now_add=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    respuesta = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Formularios_Respuesta_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Formularios_Respuesta_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Formularios_Respuesta_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Formularios_Respuesta_htmx_delete", args=(self.pk,))


class Formulario(models.Model):

    # Fields
    nombre = models.TextField(max_length=100)
    last_update = models.DateTimeField(auto_now_add=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Formularios_Formulario_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Formularios_Formulario_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Formularios_Formulario_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Formularios_Formulario_htmx_delete", args=(self.pk,))


class Pregunta(models.Model):

    # Relationships
    formulario = models.ForeignKey("Formularios.Formulario", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now=True, editable=False)
    last_update = models.DateTimeField(auto_now=True, editable=False)
    pregunta = models.TextField(max_length=200)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Formularios_Pregunta_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Formularios_Pregunta_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Formularios_Pregunta_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Formularios_Pregunta_htmx_delete", args=(self.pk,))
