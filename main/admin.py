from django.contrib import admin

# Register your models here.

from menu.models import Categories, Products

# admin.site.register(Categories)
#admin.site.register(Products)


@admin.register(Categories)
class Categories_admin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
