# coding: utf-8
from apps.accounts.models import User
from django.db import models


class Chat(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Юзер', related_name='chats')
	text = models.TextField(verbose_name=u'Сообщение')
	created_at = models.DateTimeField(verbose_name=u'Дата', auto_now_add=True)

	class Meta:
		verbose_name_plural = u'Чат'
		verbose_name = u'Чаты'