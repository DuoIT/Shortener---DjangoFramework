# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-28 04:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shorty', '0002_shortyurl_shortcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortyurl',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shortyurl',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='shortyurl',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
