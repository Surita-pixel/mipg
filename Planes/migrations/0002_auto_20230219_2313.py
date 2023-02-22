# Generated by Django 3.2.17 on 2023-02-20 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Planes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipoplanespecifico',
            name='planes_proceso',
        ),
        migrations.AddField(
            model_name='tipoplanespecifico',
            name='tipo_general',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Planes.tipoplan'),
            preserve_default=False,
        ),
    ]