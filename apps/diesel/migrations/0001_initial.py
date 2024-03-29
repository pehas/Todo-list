# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('views', models.PositiveIntegerField(verbose_name='\u0421\u0447\u0435\u0442\u0447\u0438\u043a')),
                ('views_diff', models.PositiveIntegerField(verbose_name='\u0420\u0430\u0437\u043d\u0438\u0446\u0430')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f')),
            ],
            options={
                'ordering': ['-datetime'],
                'verbose_name': '\u0417\u0430\u043f\u0438\u0441\u0438',
                'verbose_name_plural': '\u0417\u0430\u043f\u0438\u0441\u0438',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=256, verbose_name='\u042e\u0437\u0435\u0440')),
                ('pwd', models.CharField(max_length=256, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c')),
                ('url', models.URLField(verbose_name='URl')),
                ('title', models.CharField(max_length=256, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('count', models.DecimalField(verbose_name='\u0421\u0447\u0435\u0442\u0447\u0438\u043a', max_digits=10000, decimal_places=0)),
                ('last_up', models.DateTimeField(auto_now=True, verbose_name='\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u0430\u043f')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043e')),
                ('deleted', models.BooleanField(default=False, verbose_name='\u0423\u0434\u0430\u043b\u0438\u0442\u044c')),
            ],
            options={
                'ordering': ['-last_up'],
                'verbose_name': '\u0422\u043e\u043f\u0438\u043a\u0438',
                'verbose_name_plural': '\u0422\u043e\u043f\u0438\u043a\u0438',
            },
        ),
        migrations.AddField(
            model_name='log',
            name='topic',
            field=models.ForeignKey(verbose_name='\u0422\u043e\u043f\u0438\u043a', to='diesel.Topic'),
        ),
    ]
