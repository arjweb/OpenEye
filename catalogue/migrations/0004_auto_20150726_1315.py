# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicarea',
            name='curator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
