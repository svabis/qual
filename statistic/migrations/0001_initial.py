# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ip_hit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_ip', models.CharField(max_length=20)),
                ('ip_time', models.DateTimeField(null=True, blank=True)),
                ('ip_hit', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ip_hit',
            },
        ),
        migrations.CreateModel(
            name='Ip_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_ip', models.CharField(max_length=20)),
                ('ip_remark', models.CharField(max_length=200, blank=True)),
                ('ip_time', models.DateTimeField(null=True, blank=True)),
                ('ip_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'ip_list',
            },
        ),
    ]
