# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0016_remove_mapplot_radio'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapplot',
            name='radio',
            field=models.ForeignKey(default=1, to='mapplot.MapPlotType'),
        ),
    ]
