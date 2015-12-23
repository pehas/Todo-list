# -*- coding: utf-8 -*-
from decimal import Decimal
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager



AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = True
AbstractUser._meta.get_field('first_name').blank = True
AbstractUser._meta.get_field('last_name').blank = True


class User(AbstractUser):
    phone = models.CharField(verbose_name=u'Телефон', max_length=256, validators=[MinLengthValidator(4)])
