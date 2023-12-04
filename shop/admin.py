from .models import Category, Product, Tag
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category',]
    list_editable = ['price',]
    list_per_page = 10

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)