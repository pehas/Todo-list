# coding: utf-8
from django.db import models
from django.db.models.aggregates import Sum, Avg, Count


class Category(models.Model):
	title = models.CharField(verbose_name=u'Заголовок', max_length=256)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'Категория'
		verbose_name_plural = u'Категории'


class Category_item(models.Model):
	category = models.ForeignKey(Category, verbose_name=u'Категория', related_name='category_items')
	title = models.CharField(verbose_name=u'Заголовок', max_length=256)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'Тематика'
		verbose_name_plural = u'Тематики'


class Item(models.Model):
	category_item = models.ForeignKey(Category_item, verbose_name=u'Тема', related_name='items')
	money = models.DecimalField(verbose_name=u'Деньги', max_digits=1000000, decimal_places=0)
	created = models.DateTimeField(verbose_name=u'Создан', auto_now_add=True)

	def __str__(self):
		return '%s' % self.category_item

	class Meta:
		verbose_name = u'Тема'
		verbose_name_plural = u'Темы'