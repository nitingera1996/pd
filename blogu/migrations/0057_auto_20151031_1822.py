# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogu', '0056_auto_20151030_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogId',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id1', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to=b'logo_images', blank=True)),
                ('date_registered', models.DateTimeField(default=datetime.datetime(2015, 10, 31, 18, 22, 4, 256000))),
                ('address', models.CharField(max_length=300)),
                ('about', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UnPostedBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('datetime_added', models.DateTimeField(default=datetime.datetime(2015, 10, 31, 18, 22, 4, 257000))),
                ('category', models.ForeignKey(to='blogu.Category')),
                ('written_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 18, 22, 4, 254000)),
        ),
        migrations.AlterField(
            model_name='discuss',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 18, 22, 4, 271000)),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='started_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 18, 22, 4, 270000)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 31, 18, 22, 4, 259000)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='myreading_list',
            field=models.ManyToManyField(to='blogu.BlogId'),
        ),
    ]
