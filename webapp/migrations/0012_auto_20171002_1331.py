# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20171002_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='862', max_length=100),
        ),
    ]
