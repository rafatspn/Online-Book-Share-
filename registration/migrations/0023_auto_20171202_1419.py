# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-02 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlibrary',
            name='category',
            field=models.CharField(blank=True, choices=[('Educational', 'Educational'), ('Scientific', 'Scientific'), ('Fantasy', 'Fantasy'), ('Literature', 'Literature'), ('Detective', 'Detective'), ('Mystery', 'Mystery'), ('Horror', 'Horror'), ('Travel', 'Travel'), ('History', 'History'), ('Poetry', 'Poetry'), ('Journals', 'Journals'), ('Biographies', 'Biographies')], default='', max_length=100),
        ),
    ]
