# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20150727_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogueitem',
            name='level',
            field=models.ForeignKey(to='catalogue.Level'),
        ),
        migrations.AlterField(
            model_name='catalogueitem',
            name='topic_area',
            field=models.ForeignKey(to='catalogue.TopicArea'),
        ),
    ]
