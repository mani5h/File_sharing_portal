# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 08:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20171002_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='viewed',
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='333', max_length=100),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='send_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]