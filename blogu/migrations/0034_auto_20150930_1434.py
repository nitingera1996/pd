# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0033_auto_20150920_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_description',
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 30, 14, 34, 40, 586223)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 30, 14, 34, 40, 587515)),
        ),
    ]
