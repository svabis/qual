# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0006_remove_mapplot_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapplotcity',
            name='lat',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='mapplotcity',
            name='lon',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='mapplotcity',
            name='zoom',
            field=models.IntegerField(default=14),
        ),
    ]
