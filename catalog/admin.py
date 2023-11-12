from django.contrib import admin

from catalog.models import Product, Category, Version


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


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'version_number', 'name_version', 'flag_of_the_cur_ver',)
    list_filter = ('name_product', 'flag_of_the_cur_ver',)
    search_fields = ('id', 'name_product', 'version_number', 'name_version', 'flag_of_the_cur_ver',)