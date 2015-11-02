# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0059_auto_20151031_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image',
            new_name='blog_content',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='text',
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 54, 7, 553000)),
        ),
        migrations.AlterField(
            model_name='company',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 54, 7, 557000)),
        ),
        migrations.AlterField(
            model_name='discuss',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 54, 7, 571000)),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='started_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 54, 7, 570000)),
        ),
        migrations.AlterField(
            model_name='unpostedblog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 54, 7, 559000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 20, 54, 7, 561000)),
        ),
    ]
