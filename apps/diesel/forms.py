# -*- coding: utf-8 -*
import re
from grab import Grab

from django.conf import settings

from django import forms
from django.utils.translation import ugettext as _

from .models import Topic


class TopicForm(forms.ModelForm):
	password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput(), help_text=u'на diesel.elcat.kg')

	class Meta:
		model = Topic
		fields = ['url', 'login', 'password']

	def clean_url(self):
		url = self.cleaned_data['url']
		url_regex = 'https?:\/\/diesel.elcat.kg\/index.php\?showtopic=([\d]+).*'
		compiled_url_regex = re.compile(url_regex)
		urls = compiled_url_regex.findall(url)
		if urls:
			real_url = 'http://diesel.elcat.kg/index.php?showtopic=' + urls[0]
			g = Grab()
			g.setup(
				connect_timeout=30,
				timeout=60
			)

			try:
				g.go(url=real_url)
			except:
				raise forms.ValidationError(u'Что то пошло не так.')

			html = g.response.body
			mes_regex = '<div class="([\w]+)" id=\\\'([\w]+)-([\d]+)\\\'>'
			compiled_mes_regex = re.compile(mes_regex)
			topics = compiled_mes_regex.findall(html)
			if not topics:
				raise forms.ValidationError(u'Топик не существует или удален.')

			return real_url
		else:
			raise forms.ValidationError(u'Не коректный url!')

	def clean(self):
		cleaned_data = super(TopicForm, self).clean()
		if 'login' not in cleaned_data:
			return cleaned_data
		login = cleaned_data['login'].encode('cp1251')
		if 'password' not in cleaned_data:
			return cleaned_data
		password = cleaned_data['password'].encode('cp1251')
		g = Grab()
		data = {
			'UserName': login,
			'PassWord': password,
		}
		g.setup(
			post=data,
			connect_timeout=30,
			timeout=60
		)

		try:
			g.go('http://diesel.elcat.kg/index.php?act=Login&CODE=01&CookieDate=1')
		except:
			raise forms.ValidationError(_('Something went wrong, please try again later.'))
		html = g.response.body
		ent_regex = 'function moz_redirect'
		compiled_ent_regex = re.compile(ent_regex)
		entry = compiled_ent_regex.findall(html)
		if not entry:
			raise forms.ValidationError(_('Invalid login or password.'))
		url = cleaned_data['url']
		try:
			g.go(url=url)
		except:
			raise forms.ValidationError(_('Something went wrong, please try again later.'))

		html = g.response.body
		log_regex = '<a href="javascript:;" title=".*?"><b>(.+?)</b></a>'
		compiled_log_regex = re.compile(log_regex)
		topic_login = compiled_log_regex.findall(html)[0]
		if topic_login.lower() != login.lower():
			raise forms.ValidationError(_('You can not UP someone else\'s topic! Topic Starter <b>') + topic_login.decode('cp1251') + _('</b>, you logged in as <b>') + login.decode('cp1251') + ('</b>.'))
		return cleaned_data
