# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render
from apps.todo.models import Todo

from apps.todo.forms import TodoForm


def home(request):
	context = {}
	context['todos'] = Todo.objects.all()
	context['form'] = TodoForm(request.POST or None)
	if context['form'].is_valid():
		context['form'].save()
	return render(request, 'main.html', context)


def del_todo(request, id):
	Todo.objects.get(id=id).delete()
	return HttpResponse('Задача удалена')