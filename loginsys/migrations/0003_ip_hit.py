# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_auto_20170221_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip_hit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_ip', models.CharField(max_length=20)),
                ('ip_time', models.DateTimeField(null=True, blank=True)),
                ('ip_hit', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ip_hit',
            },
        ),
    ]
