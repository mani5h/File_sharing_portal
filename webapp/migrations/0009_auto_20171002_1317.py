# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 07:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0008_auto_20170906_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='send_to',
            field=models.ForeignKey(blank=None, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='130', max_length=100),
        ),
    ]
