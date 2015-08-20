# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0003_auto_20150811_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_added',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time_added',
            field=models.TimeField(blank=True),
        ),
    ]
