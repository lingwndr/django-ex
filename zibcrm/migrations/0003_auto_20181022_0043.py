# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-21 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zibcrm', '0002_auto_20181022_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='store',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='zibcrm.Store'),
            preserve_default=False,
        ),
    ]