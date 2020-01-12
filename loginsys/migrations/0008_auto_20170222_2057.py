# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0007_auto_20170222_2052'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ip_hit',
        ),
        migrations.DeleteModel(
            name='Ip_list',
        ),
    ]
