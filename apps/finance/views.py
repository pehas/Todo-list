from django.db.models.aggregates import Sum
from django.shortcuts import render

from .models import Category, Category_item, Item

from .forms import CategoryForm, CategoryItemForm, ItemForm


def category(request, id):
	context = {}
	context['category'] = Category.objects.get(id=id)
	context['category_items'] = Category_item.objects.filter(category=context['category'])
	return render(request, 'finance/category.html', context)