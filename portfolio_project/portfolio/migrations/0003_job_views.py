# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20150123_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='views',
            field=models.ImageField(default=0, upload_to=b''),
            preserve_default=True,
        ),
    ]
