# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-27 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0019_auto_20171124_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='isFavorite',
            field=models.BooleanField(default=False),
        ),
    ]
