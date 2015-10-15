# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0041_auto_20151014_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discuss',
            name='dicuss_on',
        ),
        migrations.RemoveField(
            model_name='discuss',
            name='discuss_by',
        ),
        migrations.RemoveField(
            model_name='discussion',
            name='started_by',
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 23, 52, 14, 421000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 23, 52, 14, 426000)),
        ),
        migrations.DeleteModel(
            name='Discuss',
        ),
        migrations.DeleteModel(
            name='Discussion',
        ),
    ]
