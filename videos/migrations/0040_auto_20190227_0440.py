# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-02-27 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0039_auto_20190227_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scene',
            name='hash',
            field=models.CharField(max_length=32),
        ),
    ]
