from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("PlanDeDesarrollo", api.PlanDeDesarrolloViewSet)
router.register("Informe", api.InformeViewSet)
router.register("Plan", api.PlanViewSet)
router.register("Proyecto", api.ProyectoViewSet)
router.register("Campo", api.CampoViewSet)
router.register("evidencia", api.evidenciaViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("estructura/PlanDeDesarrollo/", views.PlanDeDesarrolloListView.as_view(), name="estructura_PlanDeDesarrollo_list"),
    path("estructura/PlanDeDesarrollo/create/", views.PlanDeDesarrolloCreateView.as_view(), name="estructura_PlanDeDesarrollo_create"),
    path("estructura/PlanDeDesarrollo/detail/<int:pk>/", views.PlanDeDesarrolloDetailView.as_view(), name="estructura_PlanDeDesarrollo_detail"),
    path("estructura/PlanDeDesarrollo/update/<int:pk>/", views.PlanDeDesarrolloUpdateView.as_view(), name="estructura_PlanDeDesarrollo_update"),
    path("estructura/PlanDeDesarrollo/delete/<int:pk>/", views.PlanDeDesarrolloDeleteView.as_view(), name="estructura_PlanDeDesarrollo_delete"),
    path("estructura/Informe/", views.InformeListView.as_view(), name="estructura_Informe_list"),
    path("estructura/Informe/create/", views.InformeCreateView.as_view(), name="estructura_Informe_create"),
    path("estructura/Informe/detail/<int:pk>/", views.InformeDetailView.as_view(), name="estructura_Informe_detail"),
    path("estructura/Informe/update/<int:pk>/", views.InformeUpdateView.as_view(), name="estructura_Informe_update"),
    path("estructura/Informe/delete/<int:pk>/", views.InformeDeleteView.as_view(), name="estructura_Informe_delete"),
    path("estructura/Plan/", views.PlanListView.as_view(), name="estructura_Plan_list"),
    path("estructura/Plan/create/", views.PlanCreateView.as_view(), name="estructura_Plan_create"),
    path("estructura/Plan/detail/<int:pk>/", views.PlanDetailView.as_view(), name="estructura_Plan_detail"),
    path("estructura/Plan/update/<int:pk>/", views.PlanUpdateView.as_view(), name="estructura_Plan_update"),
    path("estructura/Plan/delete/<int:pk>/", views.PlanDeleteView.as_view(), name="estructura_Plan_delete"),
    path("estructura/Proyecto/", views.ProyectoListView.as_view(), name="estructura_Proyecto_list"),
    path("estructura/Proyecto/create/", views.ProyectoCreateView.as_view(), name="estructura_Proyecto_create"),
    path("estructura/Proyecto/detail/<int:pk>/", views.ProyectoDetailView.as_view(), name="estructura_Proyecto_detail"),
    path("estructura/Proyecto/update/<int:pk>/", views.ProyectoUpdateView.as_view(), name="estructura_Proyecto_update"),
    path("estructura/Proyecto/delete/<int:pk>/", views.ProyectoDeleteView.as_view(), name="estructura_Proyecto_delete"),
    path("estructura/Campo/", views.CampoListView.as_view(), name="estructura_Campo_list"),
    path("estructura/Campo/create/", views.CampoCreateView.as_view(), name="estructura_Campo_create"),
    path("estructura/Campo/detail/<int:pk>/", views.CampoDetailView.as_view(), name="estructura_Campo_detail"),
    path("estructura/Campo/update/<int:pk>/", views.CampoUpdateView.as_view(), name="estructura_Campo_update"),
    path("estructura/Campo/delete/<int:pk>/", views.CampoDeleteView.as_view(), name="estructura_Campo_delete"),
    path("estructura/evidencia/", views.evidenciaListView.as_view(), name="estructura_evidencia_list"),
    path("estructura/evidencia/create/", views.evidenciaCreateView.as_view(), name="estructura_evidencia_create"),
    path("estructura/evidencia/detail/<int:pk>/", views.evidenciaDetailView.as_view(), name="estructura_evidencia_detail"),
    path("estructura/evidencia/update/<int:pk>/", views.evidenciaUpdateView.as_view(), name="estructura_evidencia_update"),
    path("estructura/evidencia/delete/<int:pk>/", views.evidenciaDeleteView.as_view(), name="estructura_evidencia_delete"),
)
