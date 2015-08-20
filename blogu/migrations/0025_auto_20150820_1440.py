# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0024_auto_20150817_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='liked_blogs',
            field=models.ManyToManyField(to='blogu.Blog'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='liked_categories',
            field=models.ManyToManyField(to='blogu.Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 14, 40, 52, 983000)),
        ),
    ]
