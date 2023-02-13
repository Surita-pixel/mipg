import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from Departamentos import models as Departamentos_models
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


def create_Departamentos_Plan(**kwargs):
    defaults = {}
    defaults["nombre_plan"] = ""
    if "oficina" not in kwargs:
        defaults["oficina"] = create_Departamentos_Oficina()
    defaults.update(**kwargs)
    return Departamentos_models.Plan.objects.create(**defaults)
def create_Departamentos_Oficina(**kwargs):
    defaults = {}
    defaults["nombre_oficina"] = ""
    defaults.update(**kwargs)
    return Departamentos_models.Oficina.objects.create(**defaults)
def create_Formularios_Pregunta(**kwargs):
    defaults = {}
    defaults["pregunta"] = ""
    defaults.update(**kwargs)
    return Formularios_models.Pregunta.objects.create(**defaults)
def create_Formularios_Respuesta(**kwargs):
    defaults = {}
    defaults["respuesta"] = ""
    if "pregunta" not in kwargs:
        defaults["pregunta"] = create_Formularios_Pregunta()
    defaults.update(**kwargs)
    return Formularios_models.Respuesta.objects.create(**defaults)
def create_Formularios_Formulario(**kwargs):
    defaults = {}
    defaults["nombre"] = ""
    if "preguntas_formulario" not in kwargs:
        defaults["preguntas_formulario"] = create_Formularios_Pregunta()
    if "respuestas_formulario" not in kwargs:
        defaults["respuestas_formulario"] = create_Formularios_Respuesta()
    defaults.update(**kwargs)
    return Formularios_models.Formulario.objects.create(**defaults)
def create_Seguimientos_Formulario_Seguimiento(**kwargs):
    defaults = {}
    defaults["seguimiento_name"] = ""
    if "Formulario_Seguimiento_Plan" not in kwargs:
        defaults["Formulario_Seguimiento_Plan"] = create_Departamentos_Plan()
    if "Formulario_Seguimiento" not in kwargs:
        defaults["Formulario_Seguimiento"] = create_Formularios_Formulario()
    defaults.update(**kwargs)
    return Seguimientos_models.Formulario_Seguimiento.objects.create(**defaults)
def create_Seguimientos_Seguimiento(**kwargs):
    defaults = {}
    if "seguimiento_formulario_pivot" not in kwargs:
        defaults["seguimiento_formulario_pivot"] = create_Seguimientos_Formulario_Seguimiento()
    if "oficina" not in kwargs:
        defaults["oficina"] = create_Departamentos_Oficina()
    defaults.update(**kwargs)
    return Seguimientos_models.Seguimiento.objects.create(**defaults)
