from django.urls import path, include
from rest_framework import routers
from django.contrib.auth.decorators import login_required

from . import api
from . import views

router = routers.DefaultRouter()
router.register("Usuario", api.UsuarioViewSet)

urlpatterns = (
    path("login/", views.login, name="login"),
    path("search/", views.buscar_usuario, name="search"),
    path("", views.index, name="home"),
)
