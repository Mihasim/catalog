from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'category',)
    list_filter = ('category',)
    search_fields = ('id', 'name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)
    search_fields = ('id', 'name', 'description',)