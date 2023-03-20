from django.shortcuts import redirect, render
from apps.Usuarios.forms import LoginForm
from django.contrib.auth import  login
from apps.Usuarios.authbackend import LDAPAuthentication
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from apps.Usuarios.ldap import Ldap
from rest_framework.response import Response

from . import models
from .forms import LoginForm
from .ldap import Ldap
from django.contrib.auth.models import Group



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
    data = {}
    if request.method == "GET":
        user = models.Usuario.objects.get(id=pk)
        roles = ', '.join(map(str, user.groups.all()))
        t_rol = Group.objects.all()
        return render(request, 'editar_usuario.html', {'user': user, 'data': roles, 't_rol': t_rol})

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
        for rol in roles:
            user_id.groups.add(rol)
        return redirect('buscar_usuario')