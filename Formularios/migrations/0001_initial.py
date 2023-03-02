# Generated by Django 3.2.18 on 2023-03-02 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField(max_length=200)),
                ('created', models.DateTimeField(auto_now=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formularios.formulario')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('respuesta', models.TextField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formularios.pregunta')),
            ],
        ),
    ]
