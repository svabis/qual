# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0015_username_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='username_list',
            name='user_email',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='username_list',
            name='username',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
