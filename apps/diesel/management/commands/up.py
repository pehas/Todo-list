# -*- coding: utf-8 -*-
import threading

import datetime
import time

from django.utils import timezone
from django.core.management.base import BaseCommand
from decimal import Decimal

from ...models import Topic


def up_user(login):
	topics = Topic.objects.filter(login__iexact=login, public=True, deleted=False)
	for topic in topics:
		time_to_up = topic.last_up + datetime.timedelta(hours=topic.repeat.hour, minutes=topic.repeat.minute)
		time_now = timezone.now()
		if time_to_up < time_now:
			status = topic.up()
		else:
			status = 'not time'
		print ('%s UP-%s: %s' % (datetime.datetime.now(), status, topic.id))
		if not status:
			print topic.url


class Command(BaseCommand):
	def handle(self, *args, **options):
		topics = Topic.objects.all()

		logins = set([topic.login for topic in topics])
		for login in logins:
			up_thread = threading.Thread(target=up_user, args=[login])
			up_thread.start()