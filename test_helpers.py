import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from Departamentos import models as Departamentos_models
from Planes import models as Planes_models
from Formularios import models as Formularios_models
from Seguimientos import models as Seguimientos_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_Departamentos_Oficina(**kwargs):
    defaults = {}
    defaults["nombre_oficina"] = ""
    defaults.update(**kwargs)
    return Departamentos_models.Oficina.objects.create(**defaults)
def create_Planes_PlanEstrategico(**kwargs):
    defaults = {}
    defaults["plan_estrategico"] = ""
    if "seguimiento_plan_estrategico" not in kwargs:
        defaults["seguimiento_plan_estrategico"] = create_Seguimientos_Seguimiento()
    if "planes_inversion" not in kwargs:
        defaults["planes_inversion"] = create_Planes_PlanInversion()
    defaults.update(**kwargs)
    return Planes_models.PlanEstrategico.objects.create(**defaults)
def create_Planes_TipoPlan(**kwargs):
    defaults = {}
    defaults["nombre_tipo_plan"] = ""
    if "plan_proceso" not in kwargs:
        defaults["plan_proceso"] = create_Planes_PlanProceso()
    if "planes_especificos" not in kwargs:
        defaults["planes_especificos"] = create_Planes_TipoPlanEspecifico()
    defaults.update(**kwargs)
    return Planes_models.TipoPlan.objects.create(**defaults)
def create_Planes_PlanInversion(**kwargs):
    defaults = {}
    if "formulario_inversion" not in kwargs:
        defaults["formulario_inversion"] = create_Formularios_Formulario()
    defaults.update(**kwargs)
    return Planes_models.PlanInversion.objects.create(**defaults)
def create_Planes_PlanProceso(**kwargs):
    defaults = {}
    defaults["nombre_plan_proceso"] = ""
    if "planes_de_inversion" not in kwargs:
        defaults["planes_de_inversion"] = create_Planes_PlanInversion()
    if "seguimiento_proceso" not in kwargs:
        defaults["seguimiento_proceso"] = create_Seguimientos_Seguimiento()
    defaults.update(**kwargs)
    return Planes_models.PlanProceso.objects.create(**defaults)
def create_Planes_Plan(**kwargs):
    defaults = {}
    defaults["plan"] = ""
    if "oficina" not in kwargs:
        defaults["oficina"] = create_Departamentos_Oficina()
    if "planes_desarrollo" not in kwargs:
        defaults["planes_desarrollo"] = create_Planes_Plan_desarrollo()
    defaults.update(**kwargs)
    return Planes_models.Plan.objects.create(**defaults)
def create_Planes_PlanDesarrollo(**kwargs):
    defaults = {}
    defaults["plan_desarrollo"] = ""
    if "formulario_plan_desarrollo" not in kwargs:
        defaults["formulario_plan_desarrollo"] = create_Formularios_Formulario()
    if "planes_estrategicos" not in kwargs:
        defaults["planes_estrategicos"] = create_Planes_PlanEstrategico()
    defaults.update(**kwargs)
    return Planes_models.PlanDesarrollo.objects.create(**defaults)
def create_Planes_TipoPlanEspecifico(**kwargs):
    defaults = {}
    defaults["nombre_plan_especifico"] = ""
    if "planes_proceso" not in kwargs:
        defaults["planes_proceso"] = create_Planes_PlanProceso()
    defaults.update(**kwargs)
    return Planes_models.TipoPlanEspecifico.objects.create(**defaults)
def create_Formularios_Respuesta(**kwargs):
    defaults = {}
    defaults["respuesta"] = ""
    if "pregunta" not in kwargs:
        defaults["pregunta"] = create_Formularios_Pregunta()
    defaults.update(**kwargs)
    return Formularios_models.Respuesta.objects.create(**defaults)
def create_Formularios_Pregunta(**kwargs):
    defaults = {}
    defaults["pregunta"] = ""
    if "formulario" not in kwargs:
        defaults["formulario"] = create_Formularios_Formulario()
    defaults.update(**kwargs)
    return Formularios_models.Pregunta.objects.create(**defaults)
def create_Formularios_Formulario(**kwargs):
    defaults = {}
    defaults["nombre"] = ""
    defaults.update(**kwargs)
    return Formularios_models.Formulario.objects.create(**defaults)
def create_Seguimientos_Seguimiento(**kwargs):
    defaults = {}
    if "seguimiento_formulario" not in kwargs:
        defaults["seguimiento_formulario"] = create_Formularios_Formulario()
    if "oficina" not in kwargs:
        defaults["oficina"] = create_Departamentos_Oficina()
    defaults.update(**kwargs)
    return Seguimientos_models.Seguimiento.objects.create(**defaults)
