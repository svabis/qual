# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0023_user_data_user_mail_pasword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='user_mail_pasword',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
