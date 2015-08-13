# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0006_auto_20150811_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time_added',
            field=models.TimeField(default=b'00:00'),
        ),
    ]
