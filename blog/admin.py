from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Heading', 'slug', 'Content', 'image', 'date_of_creation', 'is_active', 'view_count',)
    list_filter = ('Heading',)
    search_fields = ('id', 'Heading', 'Content', 'date_of_creation',)
