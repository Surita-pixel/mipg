from django.db import models
from django.urls import reverse
from django.conf import settings


class PlanDeDesarrollo(models.Model):

    # Relationships
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Fields
    nombre = models.CharField(max_length=255)
    vigencia_fin = models.IntegerField()
    meta_nombre = models.CharField(max_length=30)
    fecha_inicio = models.DateTimeField()
    vigencia_inicio = models.IntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)
    indicador_nombre = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.nombre)

    def get_absolute_url(self):
        return reverse("estructura_PlanDeDesarrollo_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_PlanDeDesarrollo_update", args=(self.pk,))


class Informe(models.Model):

    # Relationships
    plan = models.ForeignKey("estructura.Plan", on_delete=models.CASCADE)

    # Fields
    periodo_reportado = models.CharField(max_length=30)
    creado_por = models.DateTimeField(auto_now_add=True, editable=False)
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)
    año = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.plan) + "-" + str(self.periodo_reportado) + "-" + str(self.año)

    def get_absolute_url(self):
        return reverse("estructura_Informe_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_Informe_update", args=(self.pk,))


class Plan(models.Model):

    # Relationships
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    proyecto = models.ManyToManyField("estructura.Proyecto")

    # Fields
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)
    nombre = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.nombre)

    def get_absolute_url(self):
        return reverse("estructura_Plan_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_Plan_update", args=(self.pk,))


class Proyecto(models.Model):

    # Relationships
    plan_de_desarrollo = models.ForeignKey("estructura.PlanDeDesarrollo", on_delete=models.CASCADE)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Fields
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=255)
    logro_de_ciudad = models.CharField(max_length=30)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)
    objetivo_general = models.CharField(max_length=30)
    Proposito = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.nombre)

    def get_absolute_url(self):
        return reverse("estructura_Proyecto_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_Proyecto_update", args=(self.pk,))


class Campo(models.Model):

    # Relationships
    plan = models.ManyToManyField("estructura.Plan")

    # Fields
    nombre = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    meta = models.CharField(max_length=30)
    indicador = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.nombre)

    def get_absolute_url(self):
        return reverse("estructura_Campo_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_Campo_update", args=(self.pk,))


class evidencia(models.Model):

    # Relationships
    campo = models.ForeignKey("estructura.Campo", on_delete=models.CASCADE)
    informe = models.ForeignKey("estructura.Informe", on_delete=models.CASCADE)

    # Fields
    ultima_actualizacion = models.DateTimeField(auto_now=True, editable=False)
    creado_por = models.DateTimeField(auto_now_add=True, editable=False)
    evidencia = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.evidencia) + "-" + str(self.informe)

    def get_absolute_url(self):
        return reverse("estructura_evidencia_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("estructura_evidencia_update", args=(self.pk,))
