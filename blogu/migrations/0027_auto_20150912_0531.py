# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogu', '0026_auto_20150908_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 5, 31, 19, 47196)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 5, 31, 19, 49495)),
        ),
        migrations.AddField(
            model_name='follow',
            name='Follow',
            field=models.ManyToManyField(to='blogu.UserProfile'),
        ),
        migrations.AddField(
            model_name='follow',
            name='userprofile',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
