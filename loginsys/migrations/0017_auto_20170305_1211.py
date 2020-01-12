# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0016_auto_20170305_1116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_kamera',
            options={'verbose_name': 'Lietot\u0101ju kameras'},
        ),
        migrations.AlterModelOptions(
            name='username_list',
            options={'verbose_name': 'Pieteiktie lietot\u0101jv\u0101rdi'},
        ),
    ]
