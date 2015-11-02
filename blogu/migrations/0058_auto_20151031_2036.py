# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0057_auto_20151031_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 36, 41, 138000)),
        ),
        migrations.AlterField(
            model_name='company',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 36, 41, 140000)),
        ),
        migrations.AlterField(
            model_name='discuss',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 36, 41, 156000)),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='started_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 36, 41, 153000)),
        ),
        migrations.AlterField(
            model_name='unpostedblog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 36, 41, 142000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 36, 41, 143000)),
        ),
    ]
