# coding: utf-8
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from apps.todo.models import Todo

from apps.todo.forms import TodoForm


def home(request):
	context = {}
	context['form'] = TodoForm(request.POST or None)
	if context['form'].is_valid():
		context['form'].save()
	return render(request, 'main.html', context)


def del_todo(request, id):
	Todo.objects.get(id=id).delete()
	return HttpResponse('Задача удалена')


def todos(request):
	todos = Todo.objects.all()
	if 'personal' in request.GET and request.GET['personal']:
		personal = request.GET['personal']
		todos = todos.filter(Q(personal=True))
	if 'work' in request.GET and request.GET['work']:
		work = request.GET['work']
		todos = todos.filter(Q(work=True))
	return render(request, 'results.html', locals())


def done_todo(request, id):
	context= {}
	context['todo'] = Todo.objects.get(id=id)
	if context['todo']:
		context['todo'].is_done = True
		context['todo'].save()
		return HttpResponse('Выполнено')
	else:
		return HttpResponse('Что то пошло не так')