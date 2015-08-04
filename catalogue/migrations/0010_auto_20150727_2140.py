# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_remove_catalogueitem_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogueitem',
            name='level',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='catalogueitem',
            name='topic_area',
            field=models.CharField(max_length=80),
        ),
    ]
