# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_auto_20200111_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='animaltype',
            name='a_count',
            field=models.IntegerField(default=0),
        ),
    ]
