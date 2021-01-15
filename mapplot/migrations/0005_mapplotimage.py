# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0004_auto_20210106_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPlotImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('imgage', models.ImageField(upload_to=b'mapplot/')),
                ('point', models.ForeignKey(default=1, to='mapplot.MapPlot')),
            ],
            options={
                'db_table': 'map_plot_images',
            },
        ),
    ]
