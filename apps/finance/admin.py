from django.contrib import admin

from .models import Category, Category_item, Item


admin.site.register(Category)
admin.site.register(Category_item)
admin.site.register(Item)

