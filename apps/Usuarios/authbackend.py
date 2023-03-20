import logging

from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


import ldap3
from ldap3.core import exceptions

logger = logging.getLogger(__name__)


class LDAPAuthentication(ModelBackend):
    def __init__(self):
        print("entro a LDAPAuthentication")
        self.server = ldap3.Server(settings.LDAP_HOST_SERVER, port=settings.LDAP_PORT_SERVER, use_ssl=False, get_info='ALL')
        self.user_prefix = settings.LDAP_USER_PREFIX


    def prefix_username(self, username):
        return f'{self.user_prefix}{username}'

    def authenticate(self, request, username=None, password=None):
        print("entro al backend de auth custom")
        if not username or not password:
            return None

        usernamelog = username + '@' + settings.LDAP_USER_PREFIX

        try:
            connection = ldap3.Connection(
                server=ldap3.Server(settings.LDAP_HOST_SERVER, port=settings.LDAP_PORT_SERVER, use_ssl=False, get_info='ALL'),
                user=usernamelog,
                password=password)
            connection.open()
            connection.bind()
            if connection.bind():
                print("Conexion correcta")
            else:
                raise exceptions.LDAPBindError
        except (
                exceptions.LDAPBindError,
                exceptions.LDAPUnknownAuthenticationMethodError) as e:
            logger.exception(e)
            return None

        try:
            user = get_user_model().objects.get(username=username)

        except User.DoesNotExist:
            print("no existe el usuario")
        return user

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except User.DoesNotExist:
            return None