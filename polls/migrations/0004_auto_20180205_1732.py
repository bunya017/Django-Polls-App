# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180204_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ballotpaper',
            name='active',
            field=models.BooleanField(),
        ),
    ]
