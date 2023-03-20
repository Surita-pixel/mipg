# Generated by Django 3.2.18 on 2023-03-14 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('meta', models.CharField(max_length=30)),
                ('indicador', models.CharField(max_length=30)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanDeDesarrollo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('vigencia_fin', models.IntegerField()),
                ('meta_nombre', models.CharField(max_length=30)),
                ('fecha_inicio', models.DateTimeField()),
                ('vigencia_inicio', models.IntegerField()),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('indicador_nombre', models.CharField(max_length=30)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=255)),
                ('logro_de_ciudad', models.CharField(max_length=30)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('objetivo_general', models.CharField(max_length=30)),
                ('Proposito', models.CharField(max_length=30)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('plan_de_desarrollo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estructura.plandedesarrollo')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('proyecto', models.ManyToManyField(to='estructura.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo_reportado', models.CharField(max_length=30)),
                ('creado_por', models.DateTimeField(auto_now_add=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('año', models.IntegerField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estructura.plan')),
            ],
        ),
        migrations.CreateModel(
            name='evidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('creado_por', models.DateTimeField(auto_now_add=True)),
                ('evidencia', models.CharField(max_length=30)),
                ('campo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estructura.campo')),
                ('informe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estructura.informe')),
            ],
        ),
        migrations.AddField(
            model_name='campo',
            name='plan',
            field=models.ManyToManyField(to='estructura.Plan'),
        ),
    ]
