# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0015_actor_last_lookup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='actor_tags',
            field=models.ManyToManyField(blank=True, null=True, to='videos.ActorTag'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='country_of_origin',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='ethnicity',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='height',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='measurements',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='tattoos',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='weight',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]