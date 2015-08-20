# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0007_auto_20150811_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='user',
            new_name='blog_by',
        ),
    ]
