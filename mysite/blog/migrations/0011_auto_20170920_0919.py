# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-20 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170920_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='reprintSource',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
