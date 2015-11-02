# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0058_auto_20151031_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 39, 59, 349000)),
        ),
        migrations.AlterField(
            model_name='company',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 39, 59, 351000)),
        ),
        migrations.AlterField(
            model_name='discuss',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 39, 59, 365000)),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='started_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 39, 59, 364000)),
        ),
        migrations.AlterField(
            model_name='unpostedblog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 39, 59, 353000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 39, 59, 355000)),
        ),
    ]
