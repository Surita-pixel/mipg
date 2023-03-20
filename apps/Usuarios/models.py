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


class Rol(models.Model):

    id = models.BigAutoField(primary_key=True, db_column='id_rol')
    rol = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    #logs
    ip_crea = models.CharField(max_length=15)
    ip_modifica = models.CharField(max_length=15)
    fecha_crea = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_modifica = models.DateTimeField(auto_now=True, editable=False)
    usuario_crea = models.CharField(max_length=16)
    usuario_modifica = models.CharField(max_length=16)  

    class Meta:
        db_table = 'ROL'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return str(self.rol)

class Permiso(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='id_permiso')
    nombre = models.CharField(max_length=100,)

    #logs
    ip_crea = models.CharField(max_length=15)
    ip_modifica = models.CharField(max_length=15)
    fecha_crea = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_modifica = models.DateTimeField(auto_now=True, editable=False)
    usuario_crea = models.CharField(max_length=16)
    usuario_modifica = models.CharField(max_length=16)  

    class Meta:
        verbose_name = "permiso"
        verbose_name_plural = "permisos"

    def __str__(self) -> str:
        return f'id: {self.id} - {self.nombre}'

class Rol_Permiso(models.Model):
    rol = models.ForeignKey(Rol, models.PROTECT, db_column='id_rol')
    permiso = models.ForeignKey(Permiso, models.PROTECT, db_column='id_permiso')
    
    #logs
    ip_crea = models.CharField(max_length=15)
    ip_modifica = models.CharField(max_length=15)
    fecha_crea = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_modifica = models.DateTimeField(auto_now=True, editable=False)
    usuario_crea = models.CharField(max_length=16)
    usuario_modifica = models.CharField(max_length=16)  

    class Meta:
        db_table = 'Rol_Permiso'
        unique_together = (('rol', 'permiso'),)

class Usuario_Rol(models.Model):

    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    
    #logs
    ip_crea = models.CharField(max_length=15)
    ip_modifica = models.CharField(max_length=15)
    fecha_crea = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_modifica = models.DateTimeField(auto_now=True, editable=False)
    usuario_crea = models.CharField(max_length=16)
    usuario_modifica = models.CharField(max_length=16)  

    class Meta:
        verbose_name_plural = 'Usuarios_Roles'

