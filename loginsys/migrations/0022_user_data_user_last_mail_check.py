# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0021_user_data_user_outside_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='user_last_mail_check',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
