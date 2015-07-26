# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogueItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=2000, blank=True)),
                ('topic_area', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=10)),
                ('link', models.CharField(max_length=255)),
                ('discovered_by', models.CharField(max_length=50)),
                ('what_learn', models.CharField(max_length=2000, blank=True)),
                ('how_apply', models.CharField(max_length=2000, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
