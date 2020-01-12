# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0007_bilde_bilde_patik'),
        ('loginsys', '0008_auto_20170222_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_kamera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kamera', models.ForeignKey(related_name='kamera', to='kamera.Kamera')),
                ('user', models.ForeignKey(to='loginsys.User_data')),
            ],
            options={
                'db_table': 'user_kameras',
            },
        ),
    ]
