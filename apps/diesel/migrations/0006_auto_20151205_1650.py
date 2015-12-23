# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diesel', '0005_auto_20151204_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name='\u0427\u0438\u0441\u043b\u043e \u0430\u043f\u043e\u0432', editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c'),
        ),
    ]
