# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 16:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160303_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url1',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 3, 16, 2, 15, 809036, tzinfo=utc)),
        ),
    ]