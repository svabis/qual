# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0002_ip_from'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ip_from',
            options={'verbose_name': 'IP no kurienes'},
        ),
        migrations.AlterModelOptions(
            name='ip_list',
            options={'verbose_name': 'IP adreses'},
        ),
    ]
