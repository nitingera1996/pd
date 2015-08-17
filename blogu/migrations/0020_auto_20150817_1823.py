# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0019_auto_20150817_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date_added',
            new_name='datetime_added',
        ),
    ]
