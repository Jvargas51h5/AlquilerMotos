# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0006_remove_alquiler_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='carnet',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
