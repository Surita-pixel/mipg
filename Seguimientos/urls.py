from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Seguimiento", api.SeguimientoViewSet)
router.register("Formulario_Seguimiento", api.Formulario_SeguimientoViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Seguimientos/Seguimiento/", views.SeguimientoListView.as_view(), name="Seguimientos_Seguimiento_list"),
    path("Seguimientos/Seguimiento/create/", views.SeguimientoCreateView.as_view(), name="Seguimientos_Seguimiento_create"),
    path("Seguimientos/Seguimiento/detail/<int:pk>/", views.SeguimientoDetailView.as_view(), name="Seguimientos_Seguimiento_detail"),
    path("Seguimientos/Seguimiento/update/<int:pk>/", views.SeguimientoUpdateView.as_view(), name="Seguimientos_Seguimiento_update"),
    path("Seguimientos/Seguimiento/delete/<int:pk>/", views.SeguimientoDeleteView.as_view(), name="Seguimientos_Seguimiento_delete"),
    path("Seguimientos/Formulario_Seguimiento/", views.Formulario_SeguimientoListView.as_view(), name="Seguimientos_Formulario_Seguimiento_list"),
    path("Seguimientos/Formulario_Seguimiento/create/", views.Formulario_SeguimientoCreateView.as_view(), name="Seguimientos_Formulario_Seguimiento_create"),
    path("Seguimientos/Formulario_Seguimiento/detail/<int:pk>/", views.Formulario_SeguimientoDetailView.as_view(), name="Seguimientos_Formulario_Seguimiento_detail"),
    path("Seguimientos/Formulario_Seguimiento/update/<int:pk>/", views.Formulario_SeguimientoUpdateView.as_view(), name="Seguimientos_Formulario_Seguimiento_update"),
    path("Seguimientos/Formulario_Seguimiento/delete/<int:pk>/", views.Formulario_SeguimientoDeleteView.as_view(), name="Seguimientos_Formulario_Seguimiento_delete"),

    path("Seguimientos/htmx/Seguimiento/", htmx.HTMXSeguimientoListView.as_view(), name="Seguimientos_Seguimiento_htmx_list"),
    path("Seguimientos/htmx/Seguimiento/create/", htmx.HTMXSeguimientoCreateView.as_view(), name="Seguimientos_Seguimiento_htmx_create"),
    path("Seguimientos/htmx/Seguimiento/delete/<int:pk>/", htmx.HTMXSeguimientoDeleteView.as_view(), name="Seguimientos_Seguimiento_htmx_delete"),
    path("Seguimientos/htmx/Formulario_Seguimiento/", htmx.HTMXFormulario_SeguimientoListView.as_view(), name="Seguimientos_Formulario_Seguimiento_htmx_list"),
    path("Seguimientos/htmx/Formulario_Seguimiento/create/", htmx.HTMXFormulario_SeguimientoCreateView.as_view(), name="Seguimientos_Formulario_Seguimiento_htmx_create"),
    path("Seguimientos/htmx/Formulario_Seguimiento/delete/<int:pk>/", htmx.HTMXFormulario_SeguimientoDeleteView.as_view(), name="Seguimientos_Formulario_Seguimiento_htmx_delete"),
)
