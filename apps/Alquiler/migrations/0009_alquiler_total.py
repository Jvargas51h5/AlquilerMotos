# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 00:57
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0008_auto_20171015_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='total',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20),
        ),
    ]
