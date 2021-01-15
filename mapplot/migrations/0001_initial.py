# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapPlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mark', models.CharField(default=b'', max_length=8)),
                ('lat', models.CharField(max_length=50)),
                ('lon', models.CharField(max_length=50)),
                ('radio', models.CharField(default=b'red', max_length=10, choices=[(b'yellow', b'stabs'), (b'green', b'kaste')])),
                ('chk_1', models.BooleanField(default=False)),
                ('chk_2', models.BooleanField(default=False)),
                ('chk_3', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('unique', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'map_plot_points',
            },
        ),
        migrations.CreateModel(
            name='MapPlotCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=20)),
            ],
            options={
                'db_table': 'map_plot_city',
            },
        ),
        migrations.AddField(
            model_name='mapplot',
            name='city',
            field=models.ForeignKey(default=1, to='mapplot.MapPlotCity'),
        ),
    ]
