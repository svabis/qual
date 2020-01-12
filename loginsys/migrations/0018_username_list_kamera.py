# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0017_auto_20170305_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='username_list',
            name='kamera',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
