# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0025_user_pin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_data',
            options={},
        ),
        migrations.AlterModelOptions(
            name='user_kamera',
            options={},
        ),
        migrations.AlterModelOptions(
            name='user_pin',
            options={},
        ),
        migrations.AlterModelOptions(
            name='username_list',
            options={},
        ),
    ]
