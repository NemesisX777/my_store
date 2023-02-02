from django.contrib import admin
from .models import Products, ProductCategory


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'is_active']
    list_editable = ['parent', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_active']
    list_editable = ['price', 'category', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Products, ProductsAdmin)
