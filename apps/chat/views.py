# coding: utf-8
from django.shortcuts import render

from .models import Chat
from .forms import ChatForm


def chat_form(request):
	context = {}
	context['form'] = ChatForm(request.POST or None)
	if context['form'].is_valid():
		form = context['form'].save(commit=False)
		form.user = request.user
		form.save()
	return render(request, 'chat/form.html', context)


def chat_text(request):
	context = {}
	context['chats'] = Chat.objects.all().order_by('-created_at')[:20]
	return render(request, 'chat/text.html', context)