from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Plan", api.PlanViewSet)
router.register("Oficina", api.OficinaViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Departamentos/Plan/", views.PlanListView.as_view(), name="Departamentos_Plan_list"),
    path("Departamentos/Plan/create/", views.PlanCreateView.as_view(), name="Departamentos_Plan_create"),
    path("Departamentos/Plan/detail/<int:pk>/", views.PlanDetailView.as_view(), name="Departamentos_Plan_detail"),
    path("Departamentos/Plan/update/<int:pk>/", views.PlanUpdateView.as_view(), name="Departamentos_Plan_update"),
    path("Departamentos/Plan/delete/<int:pk>/", views.PlanDeleteView.as_view(), name="Departamentos_Plan_delete"),
    path("Departamentos/Oficina/", views.OficinaListView.as_view(), name="Departamentos_Oficina_list"),
    path("Departamentos/Oficina/create/", views.OficinaCreateView.as_view(), name="Departamentos_Oficina_create"),
    path("Departamentos/Oficina/detail/<int:pk>/", views.OficinaDetailView.as_view(), name="Departamentos_Oficina_detail"),
    path("Departamentos/Oficina/update/<int:pk>/", views.OficinaUpdateView.as_view(), name="Departamentos_Oficina_update"),
    path("Departamentos/Oficina/delete/<int:pk>/", views.OficinaDeleteView.as_view(), name="Departamentos_Oficina_delete"),

    path("Departamentos/htmx/Plan/", htmx.HTMXPlanListView.as_view(), name="Departamentos_Plan_htmx_list"),
    path("Departamentos/htmx/Plan/create/", htmx.HTMXPlanCreateView.as_view(), name="Departamentos_Plan_htmx_create"),
    path("Departamentos/htmx/Plan/delete/<int:pk>/", htmx.HTMXPlanDeleteView.as_view(), name="Departamentos_Plan_htmx_delete"),
    path("Departamentos/htmx/Oficina/", htmx.HTMXOficinaListView.as_view(), name="Departamentos_Oficina_htmx_list"),
    path("Departamentos/htmx/Oficina/create/", htmx.HTMXOficinaCreateView.as_view(), name="Departamentos_Oficina_htmx_create"),
    path("Departamentos/htmx/Oficina/delete/<int:pk>/", htmx.HTMXOficinaDeleteView.as_view(), name="Departamentos_Oficina_htmx_delete"),
)
