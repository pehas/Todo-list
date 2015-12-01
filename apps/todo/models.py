# coding: utf-8
from django.db import models


class Todo(models.Model):
	title = models.CharField(verbose_name=u'Заголовок', max_length=256)
	text = models.TextField(verbose_name=u'Текст')
	created = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'Задача'
		verbose_name_plural = u'Задачи'