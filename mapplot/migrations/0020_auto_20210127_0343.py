# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0019_auto_20210127_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplot',
            name='radio',
            field=models.ForeignKey(to='mapplot.MapPlotType'),
        ),
    ]
