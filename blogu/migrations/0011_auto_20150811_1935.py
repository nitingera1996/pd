# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0010_remove_blog_written_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_to',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
