from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("PlanEstrategico", api.PlanEstrategicoViewSet)
router.register("TipoPlan", api.TipoPlanViewSet)
router.register("PlanInversion", api.PlanInversionViewSet)
router.register("PlanProceso", api.PlanProcesoViewSet)
router.register("Plan", api.PlanViewSet)
router.register("PlanDesarrollo", api.PlanDesarrolloViewSet)
router.register("TipoPlanEspecifico", api.TipoPlanEspecificoViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Planes/PlanEstrategico/", views.PlanEstrategicoListView.as_view(), name="Planes_PlanEstrategico_list"),
    path("Planes/PlanEstrategico/create/", views.PlanEstrategicoCreateView.as_view(), name="Planes_PlanEstrategico_create"),
    path("Planes/PlanEstrategico/detail/<int:pk>/", views.PlanEstrategicoDetailView.as_view(), name="Planes_PlanEstrategico_detail"),
    path("Planes/PlanEstrategico/update/<int:pk>/", views.PlanEstrategicoUpdateView.as_view(), name="Planes_PlanEstrategico_update"),
    path("Planes/PlanEstrategico/delete/<int:pk>/", views.PlanEstrategicoDeleteView.as_view(), name="Planes_PlanEstrategico_delete"),
    path("Planes/TipoPlan/", views.TipoPlanListView.as_view(), name="Planes_TipoPlan_list"),
    path("Planes/TipoPlan/create/", views.TipoPlanCreateView.as_view(), name="Planes_TipoPlan_create"),
    path("Planes/TipoPlan/detail/<int:pk>/", views.TipoPlanDetailView.as_view(), name="Planes_TipoPlan_detail"),
    path("Planes/TipoPlan/update/<int:pk>/", views.TipoPlanUpdateView.as_view(), name="Planes_TipoPlan_update"),
    path("Planes/TipoPlan/delete/<int:pk>/", views.TipoPlanDeleteView.as_view(), name="Planes_TipoPlan_delete"),
    path("Planes/PlanInversion/", views.PlanInversionListView.as_view(), name="Planes_PlanInversion_list"),
    path("Planes/PlanInversion/create/", views.PlanInversionCreateView.as_view(), name="Planes_PlanInversion_create"),
    path("Planes/PlanInversion/detail/<int:pk>/", views.PlanInversionDetailView.as_view(), name="Planes_PlanInversion_detail"),
    path("Planes/PlanInversion/update/<int:pk>/", views.PlanInversionUpdateView.as_view(), name="Planes_PlanInversion_update"),
    path("Planes/PlanInversion/delete/<int:pk>/", views.PlanInversionDeleteView.as_view(), name="Planes_PlanInversion_delete"),
    path("Planes/PlanProceso/", views.PlanProcesoListView.as_view(), name="Planes_PlanProceso_list"),
    path("Planes/PlanProceso/create/", views.PlanProcesoCreateView.as_view(), name="Planes_PlanProceso_create"),
    path("Planes/PlanProceso/detail/<int:pk>/", views.PlanProcesoDetailView.as_view(), name="Planes_PlanProceso_detail"),
    path("Planes/PlanProceso/update/<int:pk>/", views.PlanProcesoUpdateView.as_view(), name="Planes_PlanProceso_update"),
    path("Planes/PlanProceso/delete/<int:pk>/", views.PlanProcesoDeleteView.as_view(), name="Planes_PlanProceso_delete"),
    path("Planes/Plan/", views.PlanListView.as_view(), name="Planes_Plan_list"),
    path("Planes/Plan/create/", views.PlanCreateView.as_view(), name="Planes_Plan_create"),
    path("Planes/Plan/detail/<int:pk>/", views.PlanDetailView.as_view(), name="Planes_Plan_detail"),
    path("Planes/Plan/update/<int:pk>/", views.PlanUpdateView.as_view(), name="Planes_Plan_update"),
    path("Planes/Plan/delete/<int:pk>/", views.PlanDeleteView.as_view(), name="Planes_Plan_delete"),
    path("Planes/PlanDesarrollo/", views.PlanDesarrolloListView.as_view(), name="Planes_PlanDesarrollo_list"),
    path("Planes/PlanDesarrollo/create/", views.PlanDesarrolloCreateView.as_view(), name="Planes_PlanDesarrollo_create"),
    path("Planes/PlanDesarrollo/detail/<int:pk>/", views.PlanDesarrolloDetailView.as_view(), name="Planes_PlanDesarrollo_detail"),
    path("Planes/PlanDesarrollo/update/<int:pk>/", views.PlanDesarrolloUpdateView.as_view(), name="Planes_PlanDesarrollo_update"),
    path("Planes/PlanDesarrollo/delete/<int:pk>/", views.PlanDesarrolloDeleteView.as_view(), name="Planes_PlanDesarrollo_delete"),
    path("Planes/TipoPlanEspecifico/", views.TipoPlanEspecificoListView.as_view(), name="Planes_TipoPlanEspecifico_list"),
    path("Planes/TipoPlanEspecifico/create/", views.TipoPlanEspecificoCreateView.as_view(), name="Planes_TipoPlanEspecifico_create"),
    path("Planes/TipoPlanEspecifico/detail/<int:pk>/", views.TipoPlanEspecificoDetailView.as_view(), name="Planes_TipoPlanEspecifico_detail"),
    path("Planes/TipoPlanEspecifico/update/<int:pk>/", views.TipoPlanEspecificoUpdateView.as_view(), name="Planes_TipoPlanEspecifico_update"),
    path("Planes/TipoPlanEspecifico/delete/<int:pk>/", views.TipoPlanEspecificoDeleteView.as_view(), name="Planes_TipoPlanEspecifico_delete"),

    path("Planes/htmx/PlanEstrategico/", htmx.HTMXPlanEstrategicoListView.as_view(), name="Planes_PlanEstrategico_htmx_list"),
    path("Planes/htmx/PlanEstrategico/create/", htmx.HTMXPlanEstrategicoCreateView.as_view(), name="Planes_PlanEstrategico_htmx_create"),
    path("Planes/htmx/PlanEstrategico/delete/<int:pk>/", htmx.HTMXPlanEstrategicoDeleteView.as_view(), name="Planes_PlanEstrategico_htmx_delete"),
    path("Planes/htmx/TipoPlan/", htmx.HTMXTipoPlanListView.as_view(), name="Planes_TipoPlan_htmx_list"),
    path("Planes/htmx/TipoPlan/create/", htmx.HTMXTipoPlanCreateView.as_view(), name="Planes_TipoPlan_htmx_create"),
    path("Planes/htmx/TipoPlan/delete/<int:pk>/", htmx.HTMXTipoPlanDeleteView.as_view(), name="Planes_TipoPlan_htmx_delete"),
    path("Planes/htmx/PlanInversion/", htmx.HTMXPlanInversionListView.as_view(), name="Planes_PlanInversion_htmx_list"),
    path("Planes/htmx/PlanInversion/create/", htmx.HTMXPlanInversionCreateView.as_view(), name="Planes_PlanInversion_htmx_create"),
    path("Planes/htmx/PlanInversion/delete/<int:pk>/", htmx.HTMXPlanInversionDeleteView.as_view(), name="Planes_PlanInversion_htmx_delete"),
    path("Planes/htmx/PlanProceso/", htmx.HTMXPlanProcesoListView.as_view(), name="Planes_PlanProceso_htmx_list"),
    path("Planes/htmx/PlanProceso/create/", htmx.HTMXPlanProcesoCreateView.as_view(), name="Planes_PlanProceso_htmx_create"),
    path("Planes/htmx/PlanProceso/delete/<int:pk>/", htmx.HTMXPlanProcesoDeleteView.as_view(), name="Planes_PlanProceso_htmx_delete"),
    path("Planes/htmx/Plan/", htmx.HTMXPlanListView.as_view(), name="Planes_Plan_htmx_list"),
    path("Planes/htmx/Plan/create/", htmx.HTMXPlanCreateView.as_view(), name="Planes_Plan_htmx_create"),
    path("Planes/htmx/Plan/delete/<int:pk>/", htmx.HTMXPlanDeleteView.as_view(), name="Planes_Plan_htmx_delete"),
    path("Planes/htmx/PlanDesarrollo/", htmx.HTMXPlanDesarrolloListView.as_view(), name="Planes_PlanDesarrollo_htmx_list"),
    path("Planes/htmx/PlanDesarrollo/create/", htmx.HTMXPlanDesarrolloCreateView.as_view(), name="Planes_PlanDesarrollo_htmx_create"),
    path("Planes/htmx/PlanDesarrollo/delete/<int:pk>/", htmx.HTMXPlanDesarrolloDeleteView.as_view(), name="Planes_PlanDesarrollo_htmx_delete"),
    path("Planes/htmx/TipoPlanEspecifico/", htmx.HTMXTipoPlanEspecificoListView.as_view(), name="Planes_TipoPlanEspecifico_htmx_list"),
    path("Planes/htmx/TipoPlanEspecifico/create/", htmx.HTMXTipoPlanEspecificoCreateView.as_view(), name="Planes_TipoPlanEspecifico_htmx_create"),
    path("Planes/htmx/TipoPlanEspecifico/delete/<int:pk>/", htmx.HTMXTipoPlanEspecificoDeleteView.as_view(), name="Planes_TipoPlanEspecifico_htmx_delete"),
)
