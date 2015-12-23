# coding: utf-8
from django import forms

from .models import Category, Category_item, Item


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['title']


class CategoryItemForm(forms.ModelForm):
	class Meta:
		model = Category_item
		fields = ['title']


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['money']