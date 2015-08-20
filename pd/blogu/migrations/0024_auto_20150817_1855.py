# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0023_auto_20150817_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date_added',
        ),
        migrations.AddField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 18, 55, 1, 559000)),
        ),
    ]
