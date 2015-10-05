# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0034_auto_20150930_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='google_id',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 6, 1, 28, 94687)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 6, 1, 28, 96000)),
        ),
    ]
