# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0035_auto_20151001_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='follow',
            name='no_followed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 14, 52, 58, 855446)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 14, 52, 58, 856690)),
        ),
    ]
