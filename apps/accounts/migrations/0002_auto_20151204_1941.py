# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=256, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
