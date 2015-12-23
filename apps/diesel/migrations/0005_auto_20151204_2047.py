# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diesel', '0004_topic_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Numbers of up', editable=False, blank=True),
        ),
    ]
