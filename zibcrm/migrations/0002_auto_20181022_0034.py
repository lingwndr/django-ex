# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-21 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zibcrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='zibcrm.Store'),
        ),
    ]