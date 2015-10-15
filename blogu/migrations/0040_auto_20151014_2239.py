# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0039_auto_20151013_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discuss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('discuss_text', models.TextField()),
                ('posted_on', models.DateTimeField(verbose_name=datetime.datetime(2015, 10, 14, 22, 39, 12, 320000))),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('started_on', models.DateTimeField(default=datetime.datetime(2015, 10, 14, 22, 39, 12, 319000))),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 22, 39, 12, 304000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 22, 39, 12, 310000)),
        ),
        migrations.AddField(
            model_name='discussion',
            name='started_by',
            field=models.ForeignKey(to='blogu.UserProfile'),
        ),
        migrations.AddField(
            model_name='discuss',
            name='dicuss_on',
            field=models.ForeignKey(to='blogu.Discussion'),
        ),
        migrations.AddField(
            model_name='discuss',
            name='discuss_by',
            field=models.ForeignKey(to='blogu.UserProfile'),
        ),
    ]
