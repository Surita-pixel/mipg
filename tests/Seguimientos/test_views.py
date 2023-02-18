import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Seguimiento_list_view(client):
    instance1 = test_helpers.create_Seguimientos_Seguimiento()
    instance2 = test_helpers.create_Seguimientos_Seguimiento()
    url = reverse("Seguimientos_Seguimiento_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Seguimiento_create_view(client):
    seguimiento_formulario = test_helpers.create_Formularios_Formulario()
    oficina = test_helpers.create_Departamentos_Oficina()
    url = reverse("Seguimientos_Seguimiento_create")
    data = {
        "seguimiento_formulario": seguimiento_formulario.pk,
        "oficina": oficina.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Seguimiento_detail_view(client):
    instance = test_helpers.create_Seguimientos_Seguimiento()
    url = reverse("Seguimientos_Seguimiento_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Seguimiento_update_view(client):
    seguimiento_formulario = test_helpers.create_Formularios_Formulario()
    oficina = test_helpers.create_Departamentos_Oficina()
    instance = test_helpers.create_Seguimientos_Seguimiento()
    url = reverse("Seguimientos_Seguimiento_update", args=[instance.pk, ])
    data = {
        "seguimiento_formulario": seguimiento_formulario.pk,
        "oficina": oficina.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
