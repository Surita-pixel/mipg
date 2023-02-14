# Generated by Django 3.2.17 on 2023-02-14 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Seguimientos', '0002_rename_seguimiento_name_formulario_seguimiento_formulario_seguimiento'),
        ('Departamentos', '0002_remove_plan_oficina'),
        ('Formularios', '0004_auto_20230214_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanInversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('formulario_inversion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formularios.formulario')),
            ],
        ),
        migrations.CreateModel(
            name='PlanProceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_proceso', models.TextField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('planes_de_inversion', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Planes.planinversion')),
                ('seguimiento_proceso', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Seguimientos.seguimiento')),
            ],
        ),
        migrations.CreateModel(
            name='PlanEstrategico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('plan_estrategico', models.TextField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('planes_inversion', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Planes.planinversion')),
                ('seguimiento_plan_estrategico', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Seguimientos.seguimiento')),
            ],
        ),
        migrations.CreateModel(
            name='PlanDesarrollo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('plan_desarrollo', models.TextField(max_length=100)),
                ('formulario_plan_desarrollo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formularios.formulario')),
                ('planes_estrategicos', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Planes.planestrategico')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('plan', models.TextField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Departamentos.oficina')),
                ('planes_desarrollo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Planes.plandesarrollo')),
            ],
        ),
    ]