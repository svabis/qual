# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0017_mapplot_radio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplot',
            name='cur_lat',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mapplot',
            name='cur_lon',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
