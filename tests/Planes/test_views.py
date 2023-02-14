import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_PlanInversion_list_view(client):
    instance1 = test_helpers.create_Planes_PlanInversion()
    instance2 = test_helpers.create_Planes_PlanInversion()
    url = reverse("Planes_PlanInversion_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_PlanInversion_create_view(client):
    formulario_inversion = test_helpers.create_Formularios_Formulario()
    url = reverse("Planes_PlanInversion_create")
    data = {
        "formulario_inversion": formulario_inversion.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanInversion_detail_view(client):
    instance = test_helpers.create_Planes_PlanInversion()
    url = reverse("Planes_PlanInversion_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_PlanInversion_update_view(client):
    formulario_inversion = test_helpers.create_Formularios_Formulario()
    instance = test_helpers.create_Planes_PlanInversion()
    url = reverse("Planes_PlanInversion_update", args=[instance.pk, ])
    data = {
        "formulario_inversion": formulario_inversion.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Plan_list_view(client):
    instance1 = test_helpers.create_Planes_Plan()
    instance2 = test_helpers.create_Planes_Plan()
    url = reverse("Planes_Plan_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Plan_create_view(client):
    planes_desarrollo = test_helpers.create_Planes_Plan_desarrollo()
    oficina = test_helpers.create_Departamentos_Oficina()
    url = reverse("Planes_Plan_create")
    data = {
        "plan": "text",
        "planes_desarrollo": planes_desarrollo.pk,
        "oficina": oficina.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Plan_detail_view(client):
    instance = test_helpers.create_Planes_Plan()
    url = reverse("Planes_Plan_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Plan_update_view(client):
    planes_desarrollo = test_helpers.create_Planes_Plan_desarrollo()
    oficina = test_helpers.create_Departamentos_Oficina()
    instance = test_helpers.create_Planes_Plan()
    url = reverse("Planes_Plan_update", args=[instance.pk, ])
    data = {
        "plan": "text",
        "planes_desarrollo": planes_desarrollo.pk,
        "oficina": oficina.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanDesarrollo_list_view(client):
    instance1 = test_helpers.create_Planes_PlanDesarrollo()
    instance2 = test_helpers.create_Planes_PlanDesarrollo()
    url = reverse("Planes_PlanDesarrollo_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_PlanDesarrollo_create_view(client):
    formulario_plan_desarrollo = test_helpers.create_Formularios_Formulario()
    planes_estrategicos = test_helpers.create_Planes_PlanEstrategico()
    url = reverse("Planes_PlanDesarrollo_create")
    data = {
        "plan_desarrollo": "text",
        "formulario_plan_desarrollo": formulario_plan_desarrollo.pk,
        "planes_estrategicos": planes_estrategicos.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanDesarrollo_detail_view(client):
    instance = test_helpers.create_Planes_PlanDesarrollo()
    url = reverse("Planes_PlanDesarrollo_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_PlanDesarrollo_update_view(client):
    formulario_plan_desarrollo = test_helpers.create_Formularios_Formulario()
    planes_estrategicos = test_helpers.create_Planes_PlanEstrategico()
    instance = test_helpers.create_Planes_PlanDesarrollo()
    url = reverse("Planes_PlanDesarrollo_update", args=[instance.pk, ])
    data = {
        "plan_desarrollo": "text",
        "formulario_plan_desarrollo": formulario_plan_desarrollo.pk,
        "planes_estrategicos": planes_estrategicos.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanEstrategico_list_view(client):
    instance1 = test_helpers.create_Planes_PlanEstrategico()
    instance2 = test_helpers.create_Planes_PlanEstrategico()
    url = reverse("Planes_PlanEstrategico_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_PlanEstrategico_create_view(client):
    planes_inversion = test_helpers.create_Planes_PlanInversion()
    seguimiento_plan_estrategico = test_helpers.create_Seguimientos_Seguimiento()
    url = reverse("Planes_PlanEstrategico_create")
    data = {
        "plan_estrategico": "text",
        "planes_inversion": planes_inversion.pk,
        "seguimiento_plan_estrategico": seguimiento_plan_estrategico.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanEstrategico_detail_view(client):
    instance = test_helpers.create_Planes_PlanEstrategico()
    url = reverse("Planes_PlanEstrategico_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_PlanEstrategico_update_view(client):
    planes_inversion = test_helpers.create_Planes_PlanInversion()
    seguimiento_plan_estrategico = test_helpers.create_Seguimientos_Seguimiento()
    instance = test_helpers.create_Planes_PlanEstrategico()
    url = reverse("Planes_PlanEstrategico_update", args=[instance.pk, ])
    data = {
        "plan_estrategico": "text",
        "planes_inversion": planes_inversion.pk,
        "seguimiento_plan_estrategico": seguimiento_plan_estrategico.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanProceso_list_view(client):
    instance1 = test_helpers.create_Planes_PlanProceso()
    instance2 = test_helpers.create_Planes_PlanProceso()
    url = reverse("Planes_PlanProceso_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_PlanProceso_create_view(client):
    seguimiento_proceso = test_helpers.create_Seguimientos_Seguimiento()
    planes_de_inversion = test_helpers.create_Planes_PlanInversion()
    url = reverse("Planes_PlanProceso_create")
    data = {
        "plan_proceso": "text",
        "seguimiento_proceso": seguimiento_proceso.pk,
        "planes_de_inversion": planes_de_inversion.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanProceso_detail_view(client):
    instance = test_helpers.create_Planes_PlanProceso()
    url = reverse("Planes_PlanProceso_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_PlanProceso_update_view(client):
    seguimiento_proceso = test_helpers.create_Seguimientos_Seguimiento()
    planes_de_inversion = test_helpers.create_Planes_PlanInversion()
    instance = test_helpers.create_Planes_PlanProceso()
    url = reverse("Planes_PlanProceso_update", args=[instance.pk, ])
    data = {
        "plan_proceso": "text",
        "seguimiento_proceso": seguimiento_proceso.pk,
        "planes_de_inversion": planes_de_inversion.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
