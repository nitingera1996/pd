# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogu', '0012_auto_20150811_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField()),
                ('likes', models.IntegerField(default=True)),
                ('comment_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('comment_to', models.ForeignKey(to='blogu.Blog')),
            ],
        ),
    ]
