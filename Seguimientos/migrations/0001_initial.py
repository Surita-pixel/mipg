# Generated by Django 3.2.17 on 2023-02-16 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Planes', '0001_initial'),
        ('Departamentos', '0001_initial'),
        ('Formularios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario_Seguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('formulario_seguimiento', models.TextField(max_length=100)),
                ('Formulario_Seguimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formularios.formulario')),
                ('Formulario_Seguimiento_Plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Planes.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Departamentos.oficina')),
                ('seguimiento_formulario_pivot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seguimientos.formulario_seguimiento')),
            ],
        ),
    ]
