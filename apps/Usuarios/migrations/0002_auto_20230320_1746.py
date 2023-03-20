# Generated by Django 3.2.18 on 2023-03-20 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rol_permiso',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='rol_permiso',
            name='permiso',
        ),
        migrations.RemoveField(
            model_name='rol_permiso',
            name='rol',
        ),
        migrations.RemoveField(
            model_name='usuario_rol',
            name='rol',
        ),
        migrations.RemoveField(
            model_name='usuario_rol',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Permiso',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
        migrations.DeleteModel(
            name='Rol_Permiso',
        ),
        migrations.DeleteModel(
            name='Usuario_Rol',
        ),
    ]