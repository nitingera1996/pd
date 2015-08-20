# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0009_auto_20150811_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='written_by',
        ),
    ]
