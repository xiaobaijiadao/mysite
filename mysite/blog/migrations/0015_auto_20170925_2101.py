# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-25 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment_avatarsrc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='belong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pics', to='blog.Blog'),
        ),
    ]
