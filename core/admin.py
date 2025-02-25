from django.contrib import admin

from .models import Products, Blog, Category, Shirt, Brand

#admin.site.register(Products)

@admin.register(Products)
class Products(admin.ModelAdmin):
    #form = BlogAdminForm # Estilização do Form Blog do Admin
    list_display = ['name', 'mini_image']
    search_fields = ['name']

#admin.site.register(Blog)
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    #form = BlogAdminForm # Estilização do Form Blog do Admin
    list_display = ['mini_image', 'blo_title']
    search_fields = ['blo_title']
    
@admin.register(Category)
class Categoria(admin.ModelAdmin):
    list_display = ['cat_name', 'slug']
    search_fields = ['cat_name']
    
@admin.register(Shirt)
class Camisa(admin.ModelAdmin):
    list_display = ['name', 'mini_image']
    search_fields = ['name']

@admin.register(Brand)
class Marca(admin.ModelAdmin):
    list_display = ['mar_name', 'slug']
    search_fields = ['mar_name']

    