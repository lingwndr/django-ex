# Generated by Django 2.1.2 on 2018-10-23 10:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zibcrm', '0004_auto_20181022_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
