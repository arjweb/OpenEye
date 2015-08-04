# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_auto_20150727_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogueitem',
            name='level',
            field=models.CharField(default=b'1', max_length=80),
        ),
    ]
