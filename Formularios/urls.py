from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Pregunta", api.PreguntaViewSet)
router.register("Respuesta", api.RespuestaViewSet)
router.register("Formulario", api.FormularioViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Formularios/Pregunta/", views.PreguntaListAPIView.as_view(), name="Formularios_Pregunta_list"),
    path("Formularios/Pregunta/create/", views.PreguntaCreateView.as_view(), name="Formularios_Pregunta_create"),
    path("Formularios/Pregunta/detail/<int:pk>/", views.PreguntaDetailView.as_view(), name="Formularios_Pregunta_detail"),
    path("Formularios/Pregunta/update/<int:pk>/", views.PreguntaUpdateView.as_view(), name="Formularios_Pregunta_update"),
    path("Formularios/Pregunta/delete/<int:pk>/", views.PreguntaDeleteView.as_view(), name="Formularios_Pregunta_delete"),
    path("Formularios/Respuesta/", views.RespuestaListView.as_view(), name="Formularios_Respuesta_list"),
    path("Formularios/Respuesta/create/", views.RespuestaCreateView.as_view(), name="Formularios_Respuesta_create"),
    path("Formularios/Respuesta/detail/<int:pk>/", views.RespuestaDetailView.as_view(), name="Formularios_Respuesta_detail"),
    path("Formularios/Respuesta/update/<int:pk>/", views.RespuestaUpdateView.as_view(), name="Formularios_Respuesta_update"),
    path("Formularios/Respuesta/delete/<int:pk>/", views.RespuestaDeleteView.as_view(), name="Formularios_Respuesta_delete"),
    path("Formularios/Formulario/", views.FormularioListAPIView.as_view(), name="Formularios_Formulario_list"),
    path("Formularios/Formulario/create/", views.FormularioCreateAPIView.as_view(), name="Formularios_Formulario_create"),
    path("Formularios/Formulario/detail/<int:pk>/", views.FormularioDetailView.as_view(), name="Formularios_Formulario_detail"),
    path("Formularios/Formulario/update/<int:pk>/", views.FormularioUpdateView.as_view(), name="Formularios_Formulario_update"),
    path("Formularios/Formulario/delete/<int:pk>/", views.FormularioDeleteView.as_view(), name="Formularios_Formulario_delete"),

    path("Formularios/htmx/Pregunta/", htmx.HTMXPreguntaListView.as_view(), name="Formularios_Pregunta_htmx_list"),
    path("Formularios/htmx/Pregunta/create/", htmx.HTMXPreguntaCreateView.as_view(), name="Formularios_Pregunta_htmx_create"),
    path("Formularios/htmx/Pregunta/delete/<int:pk>/", htmx.HTMXPreguntaDeleteView.as_view(), name="Formularios_Pregunta_htmx_delete"),
    path("Formularios/htmx/Respuesta/", htmx.HTMXRespuestaListView.as_view(), name="Formularios_Respuesta_htmx_list"),
    path("Formularios/htmx/Respuesta/create/", htmx.HTMXRespuestaCreateView.as_view(), name="Formularios_Respuesta_htmx_create"),
    path("Formularios/htmx/Respuesta/delete/<int:pk>/", htmx.HTMXRespuestaDeleteView.as_view(), name="Formularios_Respuesta_htmx_delete"),
    path("Formularios/htmx/Formulario/", htmx.HTMXFormularioListView.as_view(), name="Formularios_Formulario_htmx_list"),
    path("Formularios/htmx/Formulario/create/", htmx.HTMXFormularioCreateView.as_view(), name="Formularios_Formulario_htmx_create"),
    path("Formularios/htmx/Formulario/delete/<int:pk>/", htmx.HTMXFormularioDeleteView.as_view(), name="Formularios_Formulario_htmx_delete"),
)
