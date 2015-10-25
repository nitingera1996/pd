# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0040_auto_20151014_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 22, 45, 13, 986000)),
        ),
        migrations.AlterField(
            model_name='discuss',
            name='posted_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 10, 14, 22, 45, 13, 999000)),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='started_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 22, 45, 13, 998000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 22, 45, 13, 989000)),
        ),
    ]
