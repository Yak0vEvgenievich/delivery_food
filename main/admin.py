from django.contrib import admin

# Register your models here.

from menu.models import Categories, Products

admin.site.register(Categories)
admin.site.register(Products)

