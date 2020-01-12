# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_ip', models.CharField(max_length=20)),
                ('ip_time', models.DateTimeField(null=True, blank=True)),
                ('ip_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'ip_list',
            },
        ),
        migrations.AlterModelOptions(
            name='user_data',
            options={'verbose_name': 'Lietot\u0101ju info'},
        ),
    ]
