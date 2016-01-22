# coding: utf-8
from time import sleep
import re
from apps import settings
from grab import Grab
from django.db import models


class Log(models.Model):
	topic = models.ForeignKey('Topic', verbose_name=u'Топик')
	views = models.PositiveIntegerField(verbose_name=u'Счетчик')
	views_diff = models.PositiveIntegerField(verbose_name=u'Разница')
	datetime = models.DateTimeField(verbose_name=u'Дата и время', auto_now=True)

	class Meta:
		ordering = ['-datetime']
		verbose_name = u'Записи'
		verbose_name_plural = u'Записи'


class Topic(models.Model):
	login = models.CharField(verbose_name=u'Логин', max_length=128, help_text=u'на diesel.elcat.kg')
	password = models.CharField(verbose_name=u'Пароль', max_length=128, help_text=u'на diesel.elcat.kg')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User', default= 0)
	url = models.URLField(verbose_name=u'URl')
	title = models.CharField(verbose_name=u'Заголовок', max_length=256)
	text = models.TextField(verbose_name=u'Текст')
	count = models.PositiveIntegerField(verbose_name=u'Число апов', default=0, blank=True, editable=False)
	views = models.PositiveIntegerField(verbose_name=u'Просмотры', null=True, blank=True)

	repeat = models.TimeField(verbose_name=u'Время', default='1:00:00', null=True, blank=True)
	last_up = models.DateTimeField(verbose_name=u'Последний ап', auto_now=True)
	created_at = models.DateTimeField(verbose_name=u'Создано', auto_now_add=True)
	deleted = models.BooleanField(verbose_name=u'Удалить', default=False)
	public = models.BooleanField(verbose_name=u'Опубликовать', default=True)

	message_title = models.CharField(verbose_name=u'заголвоок сообщения', max_length=500)

	def __unicode__(self):
		return self.title

	def up(self):
		try:
			g = Grab()

			# Вход
			data = {
				'UserName': self.login.encode('cp1251'),
				'PassWord': self.password.encode('cp1251')
			}
			g.setup(
				post=data,
				connect_timeout=30,
				timeout=60
			)
			g.go(url='http://diesel.elcat.kg/index.php?act=Login&CODE=01&CookieDate=1')

			# Переходим в тему
			g.setup(post=None)
			g.go(url=self.url + '&st=40')

			# Находим старые апы
			html = g.response.body

			# Удаляем старые апы
			del_regex = "up&#33;[\s\S]*?javascript:delete_post\('(.+?)'\)"
			compiled_del_regex = re.compile(del_regex)
			links_to_del = compiled_del_regex.findall(html)

			# обход в цикле по ссылкам, тема удал.
			for link in links_to_del:
				link = link.replace('&amp;', '&')
				g.go(url=link)
				sleep(10)
			g.go(url=self.url)

			# Апаем тему
			f = g.doc.rex_text('<input type="hidden" name="f" value="([\d]+)" />')
			t = g.doc.rex_text('<input type="hidden" name="t" value="([\d]+)" />')
			auth_key = g.doc.rex_text('<input type="hidden" name="auth_key" value="([\w]+)" />')

			data = {
				'act': 'Post',
				'CODE': '03',
				'f': f,
				't': t,
				'st': '0',
				'auth_key': auth_key,
				'fast_reply_used': '1',
				'Post': 'up!',
				'enabletrack': '1',
				'enableemo': '1',
				'enablesig': '1',
			}

			g.setup(post=data)
			g.go(url='http://diesel.elcat.kg/index.php?')

			# Title
			self.title = g.doc.rex_text('<title>(.*) - Diesel Forum</title>')

			# Views
			g.go('http://diesel.elcat.kg/index.php?showforum=' + f)
			self.views = int(g.doc.rex_text('<!-- Begin Topic Entry ' + t + ' -->[\s\S]*?<td align="center" class="row2">([\d]{1,8})[\s\S]*?<!--'))

			new_log = Log()
			new_log.topic = self
			new_log.views = self.views
			if Log.objects.filter(topic=self):
				old_views = Log.objects.filter(topic=self).order_by('-datetime')[0]
				new_log.views_diff = self.views - old_views.views
			else:
				new_log.views_diff = 0
			new_log.save()

			# Выходим
			g.go(url='http://diesel.elcat.kg/index.php?act=Login&CODE=03')

			self.count += 1
			self.save()
			return True
		except:
			return False

	class Meta:
		ordering = ['-last_up']
		verbose_name = u'Топики'
		verbose_name_plural = u'Топики'