# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0011_auto_20170224_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_kamera',
            name='user',
            field=models.ForeignKey(related_name='k', to=settings.AUTH_USER_MODEL),
        ),
    ]
