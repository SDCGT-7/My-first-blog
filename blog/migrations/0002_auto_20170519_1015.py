# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-19 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=2000),
        ),
    ]
