# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diesel', '0010_topic_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='repeat',
            field=models.TimeField(default=b'1:00:00', null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f', blank=True),
        ),
    ]
