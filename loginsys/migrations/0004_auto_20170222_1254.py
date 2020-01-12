# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0003_ip_hit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip_hit',
            name='ip_hit',
            field=models.CharField(max_length=100),
        ),
    ]
