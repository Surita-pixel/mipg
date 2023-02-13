import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Plan_list_view(client):
    instance1 = test_helpers.create_Departamentos_Plan()
    instance2 = test_helpers.create_Departamentos_Plan()
    url = reverse("Departamentos_Plan_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Plan_create_view(client):
    oficina = test_helpers.create_Departamentos_Oficina()
    url = reverse("Departamentos_Plan_create")
    data = {
        "nombre_plan": "text",
        "oficina": oficina.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Plan_detail_view(client):
    instance = test_helpers.create_Departamentos_Plan()
    url = reverse("Departamentos_Plan_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Plan_update_view(client):
    oficina = test_helpers.create_Departamentos_Oficina()
    instance = test_helpers.create_Departamentos_Plan()
    url = reverse("Departamentos_Plan_update", args=[instance.pk, ])
    data = {
        "nombre_plan": "text",
        "oficina": oficina.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Oficina_list_view(client):
    instance1 = test_helpers.create_Departamentos_Oficina()
    instance2 = test_helpers.create_Departamentos_Oficina()
    url = reverse("Departamentos_Oficina_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Oficina_create_view(client):
    url = reverse("Departamentos_Oficina_create")
    data = {
        "nombre_oficina": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Oficina_detail_view(client):
    instance = test_helpers.create_Departamentos_Oficina()
    url = reverse("Departamentos_Oficina_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Oficina_update_view(client):
    instance = test_helpers.create_Departamentos_Oficina()
    url = reverse("Departamentos_Oficina_update", args=[instance.pk, ])
    data = {
        "nombre_oficina": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
