# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0027_auto_20150912_0531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='Follow',
            new_name='followed',
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 6, 3, 33, 20067)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 6, 3, 33, 21378)),
        ),
    ]
