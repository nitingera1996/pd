# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0002_auto_20150811_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='heading',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_description',
            field=models.TextField(default=b''),
        ),
    ]
