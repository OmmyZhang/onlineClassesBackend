# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-01-31 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.CharField(max_length=128)),
                ('secret', models.CharField(max_length=128)),
            ],
        ),
    ]
