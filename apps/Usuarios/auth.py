from . import models
from apps.Usuarios.ldap import Ldap
from django.contrib.auth.backends import BaseBackend
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from apps.Usuarios.serializers import  UsuarioSerializer


from django.conf import settings
LDAP_SETTINGS = settings.LDAP_SETTINGS

class LdapAuthBackend(BaseBackend):

    def get_user(self, user_id):
        try:
            return models.Usuario.objects.get(pk=user_id)
        except models.Usuario.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None):
        if not LDAP_SETTINGS['enabled']:
            return self.authorizationUser(request, username=username, password=password)
        ldap = Ldap()
            
        if not self.is_localuser(username):
            if not LDAP_SETTINGS['created']:
                return None
            self.create_user(request,ldap)
        
        bind_login = ldap.login_user(username=username,password=password)
        valid_login = bind_login[0]
        if valid_login:
            return self.authorizationUser(request, username=username, password=False)
        return None
    
    def authorizationUser(self, request, username, password):
        res = ""
        if self.is_localuser(username):
            res = models.Usuario.objects.filter(Q(correo=username) | Q(username=username)).first()
        if res:
            if(password):
                password_valid = res.check_password(password)
                if password_valid:
                    request.user = res
                #login(request, res)
            else:
                request.user = res
                #login(request, res)
                # crear acceso por token
                try:
                    request.user.auth_token.delete()
                except Exception as e:
                    print(e)         
                try:
                    token = Token.objects.create(user=res)
                except Exception as e:
                    print(e)
            
        return request.user

    def is_localuser(self, username):
        #Consultamos si el usuario ya fue creado en la base de datos
        query_set = models.Usuario.objects.filter(Q(correo=username.lower()) | Q(username=username.lower()))
        if query_set:
            return True
        else: return False

    def create_user(self, request, ldap):
    #Creamos el usuario
        data = request.POST
        result = ldap.search_exact_user(data['username'])
        print (result)
        if result == None:
            raise Exception("Usuario no encontrado en el directorio activo")
        elif result:
            userdata = {}
            userdata['activo'] = True
            #data['nombre_usuario'] = result.get('nombre_usuario')
            userdata['dependencia'] = result.get('company')
            if not userdata['dependencia']:
                userdata['dependencia'] = "DADEP"
            userdata['correo'] = result.get('correo')
            userdata['username'] = result.get('usuario')
            userdata['usuario'] = result.get('usuario')
            userdata['password'] = make_password(result.get('password'))
            userdata['nombres'] = result.get('nombre_completo')
            userdata['apellidos'] = result.get('apellidos')
            if not userdata['apellidos']:
                    userdata['apellidos'] = "-"
            #userdata['usuario'] = result.get('nombre_usuario')
            userdata['nombre_completo'] = result.get('nombre_completo')
            userdata['perfil_id'] = 1
            userdata['contrato'] = result.get('finContrato')
            userdata['telefono'] = '3123456789'
            userdata['is_superuser'] = False

            print(userdata)
            serializer = UsuarioSerializer(data=userdata)
            print(serializer)
            try:
                if serializer.is_valid():
                    print('entra a valido serializer')
                    serializer.save()
                    return True
                else:
                    print(serializer.errors)
                    return False
            except Exception as e:
                print(e)
                return False