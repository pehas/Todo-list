# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diesel', '0002_auto_20151204_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(default=0, verbose_name=b'User', to=settings.AUTH_USER_MODEL),
        ),
    ]
