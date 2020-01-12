# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0022_user_data_user_last_mail_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='user_mail_pasword',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
