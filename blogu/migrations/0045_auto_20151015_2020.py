# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0044_auto_20151014_2355'),
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
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 15, 20, 20, 52, 54000)),
        ),
        migrations.AlterField(
            model_name='discuss',
            name='posted_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 10, 15, 20, 20, 52, 70000)),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='started_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 15, 20, 20, 52, 70000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 15, 20, 20, 52, 54000)),
        ),
    ]
