# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_auto_20171031_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='logo',
            field=models.ImageField(upload_to='albumlogos/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='325', max_length=100),
        ),
    ]