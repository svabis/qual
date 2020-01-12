# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0014_auto_20170305_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Username_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('datums', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'username_list',
            },
        ),
    ]
