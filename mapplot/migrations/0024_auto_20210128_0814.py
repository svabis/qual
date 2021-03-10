# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0023_auto_20210128_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplotimage',
            name='point',
            field=models.ForeignKey(related_name='image', default=1, to='mapplot.MapPlot'),
        ),
    ]
