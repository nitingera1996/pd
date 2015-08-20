# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0008_auto_20150811_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_by',
            new_name='written_by',
        ),
    ]
