from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create),
    path("view/<str:form_id>/", views.view_form),
    path("save/<str:form_id>/", views.submit_form),
    # view entries
    path("", views.main_dashboard),
    path("list/<str:form_id>/", views.show_form),
    path("list/<str:form_id>/submissions/", views.view_all_submission),
    path("list/<str:form_id>/<str:submission_id>/", views.view_submission),
]