# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blogu', '0036_auto_20151007_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(to='blogu.Category')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='languages',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_tag_line',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 16, 48, 10, 13418)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 16, 48, 10, 15449)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followed_tags',
            field=models.ManyToManyField(to='blogu.Tag'),
        ),
    ]
