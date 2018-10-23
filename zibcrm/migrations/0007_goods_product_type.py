# Generated by Django 2.1.2 on 2018-10-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zibcrm', '0006_auto_20181023_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='product_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'گردنبند'), (2, 'گردنبند رنگی'), (3, 'گردنبند تنیس'), (4, 'گردنبند فاور'), (5, 'دستببند'), (6, 'دستببند رنگی'), (7, 'دستببند تنیس'), (8, 'دستببند فلاور')], default=0),
            preserve_default=False,
        ),
    ]