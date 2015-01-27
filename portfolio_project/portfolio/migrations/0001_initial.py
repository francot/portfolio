# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('job_date', models.DateTimeField(null=True, blank=True)),
                ('priority', models.PositiveIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(related_name='category', to='portfolio.JobCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='secondary_category',
            field=models.ForeignKey(related_name='secondary_category', blank=True, to='portfolio.JobCategory', null=True),
            preserve_default=True,
        ),
    ]
