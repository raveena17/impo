# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-16 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_visit_report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientvisitreport',
            name='client_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business_unit.BusinessUnit', verbose_name='Client Details'),
        ),
    ]
