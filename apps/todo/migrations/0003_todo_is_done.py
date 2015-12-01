# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20151201_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e'),
        ),
    ]
