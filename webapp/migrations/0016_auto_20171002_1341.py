# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20171002_1335'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notifications',
            new_name='Notification',
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='353', max_length=100),
        ),
    ]