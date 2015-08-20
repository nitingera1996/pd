# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0022_auto_20150817_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='datetime_added',
        ),
        migrations.AddField(
            model_name='blog',
            name='date_added',
            field=models.DateTimeField(default='2015-1-1 00:00:00.000000', auto_now=True),
            preserve_default=False,
        ),
    ]
