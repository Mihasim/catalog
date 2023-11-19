from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):

    STATUS_published = 'published'
    STATUS_not_published = 'not_published'
    STATUSES = [
        (STATUS_published, 'опубликовано'),
        (STATUS_not_published, 'не опубликовано'),
    ]

    name = models.CharField(max_length=90, verbose_name='наименование')
    description = models.CharField(max_length=300, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.CharField(max_length=90, verbose_name='категория')
    purchase_price = models.IntegerField(verbose_name='цена за покупку')
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(default=timezone.now, verbose_name='дата последнего изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)
    is_published = models.CharField(max_length=20, default=STATUS_not_published, verbose_name='статус публикации',  choices=STATUSES)

    def __str__(self):
        return (f'{self.name} {self.description} {self.category} '
                f'{self.purchase_price} {self.date_of_creation} {self.last_modified_date} {self.is_published}')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            (
                'set_published',
                'can published posts'
            ),
            (
                'change_description',
                'Can change description'
            ),
            (
                'set_category',
                'Can set category'
            )
        ]


class Category(models.Model):
    name = models.CharField(max_length=90, verbose_name='наименование')
    description = models.CharField(max_length=300, verbose_name='описание')

    def __str__(self):
        return (f'{self.name} {self.description}')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Version(models.Model):
    name_product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=90, verbose_name='название версии')
    flag_of_the_cur_ver = models.BooleanField(verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.name_product} {self.version_number} {self.name_version}  {self.flag_of_the_cur_ver}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
