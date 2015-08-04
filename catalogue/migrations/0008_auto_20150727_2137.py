# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_catalogueitem_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogueitem',
            name='topic_area',
            field=models.ForeignKey(to='catalogue.TopicArea'),
        ),
    ]
