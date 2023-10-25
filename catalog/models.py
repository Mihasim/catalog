from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=90, verbose_name='наименование')
    description = models.CharField(max_length=300, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.CharField(max_length=90, verbose_name='категория')
    purchase_price = models.IntegerField(verbose_name='цена за покупку')
    date_of_creation = models.DateTimeField(verbose_name='дата создания')
    last_modified_date = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return (f'{self.name} {self.description} {self.category} '
                f'{self.purchase_price} {self.date_of_creation} {self.last_modified_date}')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Category(models.Model):
    name = models.CharField(max_length=90, verbose_name='наименование')
    description = models.CharField(max_length=300, verbose_name='описание')

    def __str__(self):
        return (f'{self.name} {self.description}')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
