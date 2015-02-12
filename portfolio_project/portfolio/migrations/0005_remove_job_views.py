# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20150125_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='views',
        ),
    ]
