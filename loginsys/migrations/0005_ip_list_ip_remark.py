# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0004_auto_20170222_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip_list',
            name='ip_remark',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
