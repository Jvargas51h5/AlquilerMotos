# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 04:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('cajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('carnet', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='alquiler',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alquiler.Cliente'),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='vehiculos',
            field=models.ManyToManyField(to='Vehiculo.Vehiculo'),
        ),
    ]