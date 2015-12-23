# -*- coding: utf-8 -*
import datetime
from random import randint
from grab import Grab
from django.shortcuts import render
from django.shortcuts import redirect

from django.http import JsonResponse, HttpResponse

from django.contrib.auth.decorators import login_required

# from django.db.models import Count
from django.db.models import Sum
from django.db.models import Avg

from .forms import TopicForm

from .models import Topic
from .models import Log


@login_required
def topics(request):
	context = {}
	context['title'] = u'Темы'
	context['now'] = datetime.datetime.now()
	context['topics_active'] = Topic.objects.filter(user=request.user.id, public=True, deleted=False)

	return render(request, 'diesel_up/topics.html', context)


def up_force(request, id):
	topic = Topic.objects.get(id=id, deleted=False)
	print topic
	topic.up()
	return HttpResponse('ok')


@login_required
def add(request):
	context = {}
	context['title'] = u'Добавить тему'
	context['form'] = TopicForm(request.POST or None)

	if request.POST and context['form'].is_valid():
		new_topic = context['form'].save()
		new_topic.user = request.user
		new_topic.save()
		new_topic.up()
		print new_topic
		return redirect(topics)
	else:
		return render(request, 'diesel_up/add_topic.html', context)


@login_required
def edit(request, id):
	context = {}
	context['title'] = u'Edit'
	instance = Topic.objects.get(id=id, deleted=False)
	form = TopicForm(request.POST or None, instance=instance)

	if form.is_valid():
		form.save()
		return redirect(topics)

	context['form'] = form
	return render(request, 'diesel_up/edit_topic.html', context)


@login_required
def deleted(request, id):
	Topic.objects.get(id=id, user=request.user).delete()
	return HttpResponse('ok')