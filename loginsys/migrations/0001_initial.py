# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_last_visit', models.DateTimeField(null=True, blank=True)),
                ('user_user', models.OneToOneField(related_name='u', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_data',
            },
        ),
    ]
