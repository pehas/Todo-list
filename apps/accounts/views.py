# -*- coding: utf-8 -*-
from decimal import Decimal
import user

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import SingUpForm


@csrf_exempt
def singup(request):
	context = {}
	context['form'] = SingUpForm(request.POST or None)

	if request.POST and context['form'].is_valid():
		new_user = context['form'].save()
		context['new_user'] = new_user
		new_user.backend = 'apps.accounts.auth.EmailOrUsernameModelBackend'
		login(request, new_user)
		return redirect('/', username=new_user.username)
	return render(request, 'accounts/singup.html', context)
