# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0016_auto_20150816_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time_added',
            field=models.TimeField(default=b'00:00.00.000000'),
        ),
    ]
