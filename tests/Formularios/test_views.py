import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Pregunta_list_view(client):
    instance1 = test_helpers.create_Formularios_Pregunta()
    instance2 = test_helpers.create_Formularios_Pregunta()
    url = reverse("Formularios_Pregunta_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Pregunta_create_view(client):
    url = reverse("Formularios_Pregunta_create")
    data = {
        "pregunta": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Pregunta_detail_view(client):
    instance = test_helpers.create_Formularios_Pregunta()
    url = reverse("Formularios_Pregunta_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Pregunta_update_view(client):
    instance = test_helpers.create_Formularios_Pregunta()
    url = reverse("Formularios_Pregunta_update", args=[instance.pk, ])
    data = {
        "pregunta": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Respuesta_list_view(client):
    instance1 = test_helpers.create_Formularios_Respuesta()
    instance2 = test_helpers.create_Formularios_Respuesta()
    url = reverse("Formularios_Respuesta_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Respuesta_create_view(client):
    pregunta = test_helpers.create_Formularios_Pregunta()
    url = reverse("Formularios_Respuesta_create")
    data = {
        "respuesta": "text",
        "pregunta": pregunta.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Respuesta_detail_view(client):
    instance = test_helpers.create_Formularios_Respuesta()
    url = reverse("Formularios_Respuesta_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Respuesta_update_view(client):
    pregunta = test_helpers.create_Formularios_Pregunta()
    instance = test_helpers.create_Formularios_Respuesta()
    url = reverse("Formularios_Respuesta_update", args=[instance.pk, ])
    data = {
        "respuesta": "text",
        "pregunta": pregunta.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Formulario_list_view(client):
    instance1 = test_helpers.create_Formularios_Formulario()
    instance2 = test_helpers.create_Formularios_Formulario()
    url = reverse("Formularios_Formulario_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Formulario_create_view(client):
    preguntas_formulario = test_helpers.create_Formularios_Pregunta()
    respuestas_formulario = test_helpers.create_Formularios_Respuesta()
    url = reverse("Formularios_Formulario_create")
    data = {
        "nombre": "text",
        "preguntas_formulario": preguntas_formulario.pk,
        "respuestas_formulario": respuestas_formulario.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Formulario_detail_view(client):
    instance = test_helpers.create_Formularios_Formulario()
    url = reverse("Formularios_Formulario_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Formulario_update_view(client):
    preguntas_formulario = test_helpers.create_Formularios_Pregunta()
    respuestas_formulario = test_helpers.create_Formularios_Respuesta()
    instance = test_helpers.create_Formularios_Formulario()
    url = reverse("Formularios_Formulario_update", args=[instance.pk, ])
    data = {
        "nombre": "text",
        "preguntas_formulario": preguntas_formulario.pk,
        "respuestas_formulario": respuestas_formulario.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
