# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diesel', '0009_auto_20151206_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(null=True, verbose_name='\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u044b', blank=True),
        ),
    ]
