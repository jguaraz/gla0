# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gl0', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='g',
            name='id_p',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='g',
            name='value',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
