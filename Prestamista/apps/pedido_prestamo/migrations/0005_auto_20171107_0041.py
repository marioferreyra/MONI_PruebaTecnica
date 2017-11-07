# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-07 00:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido_prestamo', '0004_auto_20171107_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='apellido',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='nombre',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]