# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0009_auto_20210115_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapplot',
            name='edit_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
