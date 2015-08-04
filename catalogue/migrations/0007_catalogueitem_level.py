# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20150727_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogueitem',
            name='level',
            field=models.ForeignKey(default='1', to='catalogue.Level'),
            preserve_default=False,
        ),
    ]
