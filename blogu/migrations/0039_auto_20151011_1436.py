# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0038_auto_20151007_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='google_registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='login',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 11, 14, 36, 46, 667947)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 11, 14, 36, 46, 669887)),
        ),
    ]
