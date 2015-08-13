# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_added',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='blog',
            name='heading',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time_added',
            field=models.TimeField(default=None),
        ),
    ]
