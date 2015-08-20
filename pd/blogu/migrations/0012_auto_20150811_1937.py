# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogu', '0011_auto_20150811_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=b'blog_images', blank=True)),
                ('image_description', models.TextField(default=b'')),
                ('heading', models.TextField(default=b'')),
                ('text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('date_added', models.DateField(default=b'2015-01-01')),
                ('time_added', models.TimeField(default=b'00:00')),
                ('category', models.ForeignKey(to='blogu.Category')),
                ('written_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_by',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
