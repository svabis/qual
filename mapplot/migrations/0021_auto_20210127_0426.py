# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mapplot', '0020_auto_20210127_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapplot',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mapplot',
            name='radio',
            field=models.ForeignKey(default=1, to='mapplot.MapPlotType'),
        ),
    ]
