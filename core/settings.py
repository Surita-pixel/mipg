"""
Django settings for core project.

For more information on this file, see
https://docs.djangoproject.com/

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^l)7d*%h&db4uft@dk%h-w&nup#pu%)a!d)c7jwgoixo5_hm0$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.Planes',
    'apps.Departamentos',
    'apps.Seguimientos',
    'apps.Formularios',
    'apps.Formulario',
    'apps.estructura',
    'apps.Usuarios'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME' : 'formularios_db',
		'USER' : 'postgres',
		'PASSWORD' : 'pokemon70',
		'HOST' : 'localhost', #si tienes otra dirección host debes remplazar esta
		'PORT' : '' #si lo dejas vacío tomara el puerto por default
	}
}

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mipg',
        'USER': 'postgres',
        'PASSWORD': 'Pg2021+',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}"""


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/login/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'apps/static'),
)


LDAP_SERVERS = [
    {
        'host': '172.25.1.121',
        'port': 389,
        'use_ssl': False,
        'get_info': 'NONE',
    },
    {
        'host': '172.26.1.12',
        'port': 389,
        'use_ssl': False,
        'get_info': 'NONE',
    },
]

LDAP_BIND_USER = 'agutierrezv@espacio.int'

LDAP_BIND_PWD = 'Capid2022+'

LDAP_SEARCH_BASE = ''

LDAP_USER_SEARCH_FILTER = ''


LDAP_HOST_SERVER = '172.25.1.121'

LDAP_PORT_SERVER = 389

LDAP_USER_SERVER = 'agutierrezv@espacio.int'

LDAP_PASSWORD_SERVER = 'Capid2022+'

LDAP_ENGINE = 'OpenLDAP'

LDAP_SEARCH_BASE = "dc=espacio,dc=int"

LDAP_USER_SEARCH_FILTER = "(&(sAMAccountName=%s)(objectClass=user))"

LDAP_MIN_GROUPS = ["MyDjangoGroup", ]

LDAP_SUPERUSER_GROUPS = 'agutierrezv@espacio.int'
LDAP_STAFF_GROUPS = {
    'username': 'sAMAccountName',
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
}

LDAP_ATTRIBUTES_MAP = {
    'username': 'sAMAccountName',
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
}

LDAP_GROUPS_SEARCH_FILTER =''

LDAP_GROUP_MEMBER_ATTRIBUTE= ''

LDAP_GROUPS_MAP= {
    'username': 'sAMAccountName',
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
}

LDAP_BIND_PASSWORD = ''

AUTH_LDAP_SERVER_URI = '172.25.1.121'
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s, OU=Sistemas,dc=espacio, dc=int"
AUTH_LDAP_START_TLS = True


IP_CREO_DEFAULT = '127.0.0.1'
USER_CREO_DEFAULT = 'MIPG'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


AUTH_ENABLED = True

LDAP_SETTINGS = {
    'server': '172.25.1.121',
    'port': '389',
    'user': 'dmesa',
    'password': 'Dm3s423++D',
    'enabled': True,
    'created': True

}

LDAP_SERVER = os.environ.get('LDAP_SERVER', None)
LDAP_USER_PREFIX = "espacio.int"
LDAP_USER_GROUP = os.environ.get('LDAP_USER_GROUP', None)
LDAP_STAFF_GROUP = os.environ.get('LDAP_STAFF_GROUP', None)
LDAP_ADMIN_GROUP = os.environ.get('LDAP_ADMIN_GROUP', None)
LDAP_SEARCH_BASE = os.environ.get('LDAP_SEARCH_BASE', None)
LDAP_SEARCH_FILTER = os.environ.get('LDAP_SEARCH_FILTER', None)

AUTH_USER_MODEL = 'Usuarios.Usuario'
# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'apps.Usuarios.authbackend.LDAPAuthentication',
# ]

AUTHENTICATION_BACKENDS = ('apps.Usuarios.auth.LdapAuthBackend',)