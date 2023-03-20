from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    usuario = models.CharField(max_length=16, unique=True)
    username = models.CharField(max_length=16, unique=True)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    dependencia = models.CharField(max_length=45)
    correo = models.EmailField()
    activo = models.BooleanField(default=True)
    is_staff =models.BooleanField(default=True)
    
    #logs
    ip_crea = models.CharField(max_length=15)
    ip_modifica = models.CharField(max_length=15)
    fecha_crea = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_modifica = models.DateTimeField(auto_now=True, editable=False)
    usuario_crea = models.CharField(max_length=16)
    usuario_modifica = models.CharField(max_length=16)  
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'Usuario'
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        # ordering = ['usuario']
        db_table = "Usuario"

    def __str__(self) -> str:
        return f'{self.id} - {self.nombres} {self.apellidos}'
