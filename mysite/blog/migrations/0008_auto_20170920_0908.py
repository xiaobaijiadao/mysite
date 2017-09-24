# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-20 09:08
from __future__ import unicode_literals

import blog.system.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170919_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pic',
            name='kind',
        ),
        migrations.RemoveField(
            model_name='pic',
            name='tic',
        ),
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(blank=True, storage=blog.system.storage.ImageStorage(), upload_to='blog/%Y_%m'),
        ),
    ]