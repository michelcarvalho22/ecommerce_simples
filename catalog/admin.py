# coding=utf-8

from django.contrib import admin

from .models import Product, Category,Carroucel,Cor,Tamanho


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created', 'modified']


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created', 'modified']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Carroucel)
admin.site.register(Cor)
admin.site.register(Tamanho)
