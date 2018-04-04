# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20170903_1419'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
        migrations.RenameModel(
            old_name='Songs',
            new_name='Song',
        ),
        migrations.RenameModel(
            old_name='Videos',
            new_name='Video',
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Musical ', 'Musical '), ('Jazz', 'Jazz'), ('Folk', 'Folk'), ('Hardcore', 'Hardcore'), ('Blues', 'Blues'), ('Rapping', 'Rapping')], max_length=20),
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='12', max_length=100),
        ),
    ]
