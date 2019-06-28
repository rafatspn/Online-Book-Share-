# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-23 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_userlibrary'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlibrary',
            name='author_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userlibrary',
            name='book_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userlibrary',
            name='category',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userlibrary',
            name='publishing_year',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]