# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamera', '0006_kamera_kamera_type'),
        ('loginsys', '0005_ip_list_ip_remark'),
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
