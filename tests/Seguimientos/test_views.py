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
    seguimiento_formulario_pivot = test_helpers.create_Seguimientos_Formulario_Seguimiento()
    oficina = test_helpers.create_Departamentos_Oficina()
    url = reverse("Seguimientos_Seguimiento_create")
    data = {
        "seguimiento_formulario_pivot": seguimiento_formulario_pivot.pk,
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
    seguimiento_formulario_pivot = test_helpers.create_Seguimientos_Formulario_Seguimiento()
    oficina = test_helpers.create_Departamentos_Oficina()
    instance = test_helpers.create_Seguimientos_Seguimiento()
    url = reverse("Seguimientos_Seguimiento_update", args=[instance.pk, ])
    data = {
        "seguimiento_formulario_pivot": seguimiento_formulario_pivot.pk,
        "oficina": oficina.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Formulario_Seguimiento_list_view(client):
    instance1 = test_helpers.create_Seguimientos_Formulario_Seguimiento()
    instance2 = test_helpers.create_Seguimientos_Formulario_Seguimiento()
    url = reverse("Seguimientos_Formulario_Seguimiento_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Formulario_Seguimiento_create_view(client):
    Formulario_Seguimiento = test_helpers.create_Formularios_Formulario()
    Formulario_Seguimiento_Plan = test_helpers.create_Departamentos_Plan()
    url = reverse("Seguimientos_Formulario_Seguimiento_create")
    data = {
        "formulario_seguimiento": "text",
        "Formulario_Seguimiento": Formulario_Seguimiento.pk,
        "Formulario_Seguimiento_Plan": Formulario_Seguimiento_Plan.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Formulario_Seguimiento_detail_view(client):
    instance = test_helpers.create_Seguimientos_Formulario_Seguimiento()
    url = reverse("Seguimientos_Formulario_Seguimiento_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Formulario_Seguimiento_update_view(client):
    Formulario_Seguimiento = test_helpers.create_Formularios_Formulario()
    Formulario_Seguimiento_Plan = test_helpers.create_Departamentos_Plan()
    instance = test_helpers.create_Seguimientos_Formulario_Seguimiento()
    url = reverse("Seguimientos_Formulario_Seguimiento_update", args=[instance.pk, ])
    data = {
        "formulario_seguimiento": "text",
        "Formulario_Seguimiento": Formulario_Seguimiento.pk,
        "Formulario_Seguimiento_Plan": Formulario_Seguimiento_Plan.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
