from django.shortcuts import redirect, render
from apps.Usuarios.forms import LoginForm
from apps.Usuarios.authbackend import LDAPAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from apps.Usuarios.ldap import Ldap
from rest_framework.response import Response

from . import models
from .forms import LoginForm
from .ldap import Ldap
from django.contrib.auth.models import Group

from django.contrib.auth.models import Group
from . import models


@login_required(login_url="/login/")
def index(request):
    return render(
        request,
        'index.html',
        {}
    )



"""def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = LDAPAuthentication.authenticate(request,request,username=username, password=password)

            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                request.session['UserLogued']=username
                return redirect("/")
            else:
                msg = "Credenciales incorrectas"
        else:
            msg = "Error validando el formulario"

    return render(request, "login.html", {"form": form, "msg": msg})
"""
def buscar_usuario(request):
    data = ""
    msg = ""
    usuarios = models.Usuario.objects.all()
    if request.method == "POST":
        user = request.POST['Usuario']
        ldap = Ldap()
        result = ldap.search_exact_user(user)
        roles = Group.objects.all()

        if result == None:
            msg = "Usuario no encontrado en el directorio activo"
        else:
            data = {
                'nombre_usuario': result['nombre_usuario'],
                'correo': result['correo'],
                'nombres': result['nombres'],
                'apellidos': result['apellidos'],
                'nombre_completo': result['nombre_completo'],
                'dependencia': result['dependencia'],
                'estado': result['activo'],
                'roles': roles,
            }

    return render(request, "buscar_usuario.html", {"data": data, "msg": msg, "usuarios": usuarios})


def login(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)

            ldap = Ldap()
                
            if authenticate(request, username=username, password=password):
                print("entra a login")
                return redirect("/buscar_usuario")
            else:
                msg = "Credenciales incorrectas"
    return render(request, "login.html", {"form": form, "msg": msg})

def editar_usuario(request, pk):
    if request.method == "GET":
        user = models.Usuario.objects.get(id=pk)
        # Obtener los roles del usuario y de los que no son
        user_roles = user.groups.all()
        roles = Group.objects.exclude(id__in=user_roles.values_list('id', flat=True))
        # Obtener todos los roles
        all_roles = Group.objects.all()
        # Separar los roles en dos listas: asignados y no asignados
        assigned_roles = []
        unassigned_roles = []
        for role in all_roles:
            if role in user_roles:
                assigned_roles.append(role)
            else:
                unassigned_roles.append(role)
        return render(request, 'editar_usuario.html', {'user': user, 'assigned_roles': assigned_roles, 'unassigned_roles': unassigned_roles})
    
    elif request.method == 'POST':
        roles = request.POST.getlist('roles')
        q = models.Usuario.objects.get(id=pk)
        q.usuario = request.POST.get('usuario')
        q.nombres = request.POST.get('nombres')
        q.apellidos = request.POST.get('apellidos')
        q.dependencia = request.POST.get('dependencia')
        q.correo = request.POST.get('correo')
        q.ip_crea = '127.0.0.1'
        q.ip_modifica = '127.0.0.1'
        q.usuario_crea = 'dcobos'
        q.usuario_modifica = 'dcobos'
        q.save()
        user_id = models.Usuario.objects.filter(id=pk).first()
        if user_id is None:
            pass
        else:
            user_id.groups.set(roles)
        return redirect('/buscar_usuario')
