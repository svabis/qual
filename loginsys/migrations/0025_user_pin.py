# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loginsys', '0024_auto_20170820_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_pin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_pin', models.CharField(max_length=30)),
                ('user_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_pin',
                'verbose_name': 'Lietot\u0101ju pin',
            },
        ),
    ]
