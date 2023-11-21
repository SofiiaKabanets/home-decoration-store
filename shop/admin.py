from .models import Category, Product
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'stock', 
    'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 15

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)