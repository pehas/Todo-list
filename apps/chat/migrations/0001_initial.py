# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430')),
                ('user', models.ForeignKey(related_name='chats', verbose_name='\u042e\u0437\u0435\u0440', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0427\u0430\u0442\u044b',
                'verbose_name_plural': '\u0427\u0430\u0442',
            },
        ),
    ]
