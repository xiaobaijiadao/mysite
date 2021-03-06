# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-18 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170918_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='kind',
            field=models.CharField(choices=[('code', 'code'), ('life', 'life')], max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.CharField(choices=[('python', 'python'), ('机器学习', '机器学习'), ('琐事', '琐事')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pic',
            name='kind',
            field=models.CharField(choices=[('cover', 'cover'), ('inner', 'inner')], default='cover', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='power',
            field=models.CharField(choices=[('host', 'host'), ('user', 'user'), ('vistor', 'vistor')], default='user', max_length=20),
        ),
    ]
