# Generated by Django 2.1.2 on 2018-10-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zibcrm', '0010_remove_goods_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='clean_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'SL3'), (2, 'SL2'), (3, 'SL1'), (4, 'VS2'), (5, 'VS1'), (6, 'VVS2'), (7, 'VVS1'), (8, 'IF')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='cut_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Round'), (2, 'Marquis'), (3, 'Tears'), (4, 'Bugat'), (5, 'Princesses'), (6, 'Oval '), (7, 'Trellens'), (8, 'MIX'), (9, 'Emerald'), (10, 'Terry Engel')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='felez_price',
            field=models.IntegerField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='id_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'GAI'), (2, 'HRD')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='stone_color_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'G'), (2, 'D'), (3, 'E'), (4, 'F'), (5, 'H'), (6, 'I'), (7, 'K'), (8, 'L'), (9, 'J'), (10, 'M')], default=0),
            preserve_default=False,
        ),
    ]