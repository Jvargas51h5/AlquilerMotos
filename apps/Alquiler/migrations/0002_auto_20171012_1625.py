# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]