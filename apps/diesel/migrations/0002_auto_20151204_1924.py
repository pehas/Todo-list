# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diesel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='pwd',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='user',
        ),
        migrations.AddField(
            model_name='topic',
            name='login',
            field=models.CharField(default=1, help_text='\u043d\u0430 diesel.elcat.kg', max_length=128, verbose_name='\u041b\u043e\u0433\u0438\u043d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='password',
            field=models.CharField(default=1, help_text='\u043d\u0430 diesel.elcat.kg', max_length=128, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c'),
            preserve_default=False,
        ),
    ]
