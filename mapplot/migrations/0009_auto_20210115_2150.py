# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0008_auto_20210115_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mapplot',
            old_name='date',
            new_name='create_date',
        ),
        migrations.AddField(
            model_name='mapplot',
            name='cur_lat',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='mapplot',
            name='cur_lon',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='mapplot',
            name='device',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
