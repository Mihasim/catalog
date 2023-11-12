from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    Heading = models.CharField(max_length=90, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    Content = models.CharField(max_length=300, verbose_name='Содержимое')
    image = models.ImageField(upload_to='products/', verbose_name='изображение (превью)', **NULLABLE)
    date_of_creation = models.DateField(default=timezone.now, verbose_name='дата создания')
    is_active = models.BooleanField(default=True, verbose_name='признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='Счетчик просмотров')

    def __str__(self):
        return f'{self.Heading}, {self.Content}, {self.date_of_creation}, {self.is_active}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
