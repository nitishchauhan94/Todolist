# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-10 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='Leave',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='Evening',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='General',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='Morning',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
