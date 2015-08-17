# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0017_auto_20150817_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='time_added',
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
