from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Oficina", api.OficinaViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Departamentos/Oficina/", views.OficinaListView.as_view(), name="Departamentos_Oficina_list"),
    path("Departamentos/Oficina/create/", views.OficinaCreateView.as_view(), name="Departamentos_Oficina_create"),
    path("Departamentos/Oficina/detail/<int:pk>/", views.OficinaDetailView.as_view(), name="Departamentos_Oficina_detail"),
    path("Departamentos/Oficina/update/<int:pk>/", views.OficinaUpdateView.as_view(), name="Departamentos_Oficina_update"),
    path("Departamentos/Oficina/delete/<int:pk>/", views.OficinaDeleteView.as_view(), name="Departamentos_Oficina_delete"),

    path("Departamentos/htmx/Oficina/", htmx.HTMXOficinaListView.as_view(), name="Departamentos_Oficina_htmx_list"),
    path("Departamentos/htmx/Oficina/create/", htmx.HTMXOficinaCreateView.as_view(), name="Departamentos_Oficina_htmx_create"),
    path("Departamentos/htmx/Oficina/delete/<int:pk>/", htmx.HTMXOficinaDeleteView.as_view(), name="Departamentos_Oficina_htmx_delete"),
)
