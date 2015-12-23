# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diesel', '0008_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='user',
        ),
        migrations.DeleteModel(
            name='Mail',
        ),
    ]
