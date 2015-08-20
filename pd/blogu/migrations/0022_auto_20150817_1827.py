# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0021_auto_20150817_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
