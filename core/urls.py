"""
mipg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views
from apps.Planes.views import UserView

from apps.Usuarios import views as UsuariosViews

urlpatterns = [
    path("u/", UserView.as_view(), name="User"),
    path("", UsuariosViews.index, name="index"),
    
    path("buscar_usuario/", UsuariosViews.buscar_usuario, name="search"),
    path("editar_usuario/<int:pk>/", UsuariosViews.editar_usuario, name="editar_usuario"),
    path('login/', UsuariosViews.login, name="login_ldap"),
    path('Departamentos/', include('apps.Departamentos.urls')),
    path('Planes/', include('apps.Planes.urls')),
    path('Formularios/', include('apps.Formularios.urls')),
    path('Seguimientos/', include('apps.Seguimientos.urls')),
    path('htmx/', views.htmx_home, name='htmx'),
    path('admin/', admin.site.urls),
    path('estructura/', include('apps.estructura.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('usuarios/', include('apps.Usuarios.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

