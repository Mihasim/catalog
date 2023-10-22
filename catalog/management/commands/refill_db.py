from django.core.management import BaseCommand
from django.core.management.commands import dumpdata

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        products_list = [
            {'name': 'Телеграмм бот', 'description': 'Бот для ТГ', 'image': '', 'category': 'Товар',
             'purchase_price': '1000', 'date_of_creation': '2023-1-1', 'last_modified_date': '2023-10-20'},
            {'name': 'YouTube парсер', 'description': 'парсер для YT', 'image': '', 'category': 'Товар',
             'purchase_price': '10000', 'date_of_creation': '2023-2-1',
             'last_modified_date': '2023-09-20'},
        ]

        products_for_create = []
        for products_item in products_list:
            products_for_create.append(
                Product(**products_item)
            )

        Product.objects.bulk_create(products_for_create)

        categories_list = [
            {'name': 'Товар', 'description': 'Товары магазина'},
            {'name': 'Ресурс', 'description': 'Ресурс компании'},
            {'name': 'Товар', 'description': 'Товары на продажу'},
            {'name': 'Ресурс', 'description': 'Дерево'},
            {'name': 'Товар', 'description': 'Что-то полезное'},
            {'name': 'Ресурс', 'description': 'Оборудование'},
            {'name': 'Ресурс', 'description': 'Камень'},
            {'name': 'Ресурс', 'description': 'Золото'},
        ]

        categories_for_create = []
        for categories_item in categories_list:
            categories_for_create.append(
                Category(**categories_item)
            )

        Category.objects.bulk_create(categories_for_create)

