# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['created'], 'verbose_name': '\u0417\u0430\u0434\u0430\u0447\u0430', 'verbose_name_plural': '\u0417\u0430\u0434\u0430\u0447\u0438'},
        ),
        migrations.AddField(
            model_name='todo',
            name='personal',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430'),
        ),
        migrations.AddField(
            model_name='todo',
            name='work',
            field=models.BooleanField(default=False, verbose_name='\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430'),
        ),
    ]
