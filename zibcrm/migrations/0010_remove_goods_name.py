# Generated by Django 2.1.2 on 2018-10-23 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zibcrm', '0009_auto_20181023_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='name',
        ),
    ]
