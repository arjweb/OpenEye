# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20150727_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogueitem',
            name='level',
        ),
    ]
