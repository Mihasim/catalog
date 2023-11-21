from django.conf import settings
from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def cache_category():
    """
    Кещируем категории
    "Нужно создать функцию, которая будет получать список категорий из кэша, если кэш включен.
    Класть список в кэш если кэш включен и списка в кэше нет.
    Если кэш выключен - делать запрос в ОРМ."
    """
    if CACHE_ENABLED:
        key = f'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list