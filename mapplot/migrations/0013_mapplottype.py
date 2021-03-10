# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0012_auto_20210127_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPlotType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50)),
                ('color', models.CharField(default=b'', max_length=20)),
                ('size', models.IntegerField(default=3)),
            ],
            options={
                'db_table': 'map_plot_point_type',
            },
        ),
    ]
