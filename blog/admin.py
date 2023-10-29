from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Heading', 'Content', 'image', 'is_active', 'view_count', 'slug')
    list_filter = ('Heading',)
    search_fields = ('id', 'Heading', 'Content', 'date_of_creation',)
