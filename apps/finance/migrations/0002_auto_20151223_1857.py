# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='category_item',
            options={'verbose_name': '\u0422\u0435\u043c\u0430\u0442\u0438\u043a\u0430', 'verbose_name_plural': '\u0422\u0435\u043c\u0430\u0442\u0438\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': '\u0422\u0435\u043c\u0430', 'verbose_name_plural': '\u0422\u0435\u043c\u044b'},
        ),
    ]
