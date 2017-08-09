# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_freeradius', '0005_radacct_fix_called_calling'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiuspostauth',
            name='called_station_id',
            field=models.CharField(blank=True, db_column='calledstationid', max_length=50, null=True, verbose_name='called station ID'),
        ),
        migrations.AddField(
            model_name='radiuspostauth',
            name='calling_station_id',
            field=models.CharField(blank=True, db_column='callingstationid', max_length=50, null=True, verbose_name='calling station ID'),
        ),
        migrations.AlterField(
            model_name='radiuspostauth',
            name='password',
            field=models.CharField(blank=True, db_column='pass', max_length=64, verbose_name='password'),
        ),
    ]
