# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='description',
            field=models.TextField(default='description default text'),
        ),
    ]