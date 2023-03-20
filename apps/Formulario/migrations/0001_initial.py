# Generated by Django 3.2.18 on 2023-03-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InputField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('label', models.CharField(max_length=100)),
                ('form_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InputType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('InputField', 'InputField'), ('MultipleChoiceField', 'MultipleChoiceField')], default='InputField', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('label', models.CharField(max_length=100)),
                ('form_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('question_id', models.IntegerField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('form_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ResponseQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
                ('response', models.CharField(max_length=255)),
                ('type_id', models.IntegerField(default=1)),
                ('response_id', models.IntegerField()),
            ],
        ),
    ]