# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 07:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0009_auto_20171002_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=1000)),
                ('sender', models.CharField(max_length=300)),
                ('viewed', models.BooleanField(default=False)),
                ('send_to', models.ForeignKey(blank=None, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='send_to',
        ),
        migrations.RemoveField(
            model_name='message',
            name='viewed',
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='260', max_length=100),
        ),
    ]
