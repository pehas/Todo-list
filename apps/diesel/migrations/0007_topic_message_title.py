# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diesel', '0006_auto_20151205_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='message_title',
            field=models.CharField(default=1, max_length=500, verbose_name='\u0437\u0430\u0433\u043e\u043b\u0432\u043e\u043e\u043a \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f'),
            preserve_default=False,
        ),
    ]
