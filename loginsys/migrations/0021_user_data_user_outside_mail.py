# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0020_username_list_passw'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='user_outside_mail',
            field=models.BooleanField(default=False),
        ),
    ]
