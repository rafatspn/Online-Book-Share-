# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-22 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_auto_20171122_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pro_pic',
            field=models.ImageField(blank=True, upload_to='profilepic'),
        ),
    ]
