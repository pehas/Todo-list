# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diesel', '0007_topic_message_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=500, verbose_name='\u041b\u043e\u0433\u0438\u043d')),
                ('password', models.CharField(max_length=500, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c')),
                ('title', models.CharField(max_length=500, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('user', models.ForeignKey(default=0, verbose_name=b'User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
