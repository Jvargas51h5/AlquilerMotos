# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 03:55
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('latitud', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20)),
                ('longitud', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20)),
                ('vehiculo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Vehiculo.Vehiculo')),
            ],
        ),
    ]