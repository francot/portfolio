# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_job_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
