from django.contrib.auth.models import AbstractUser
from django.db import models

from random import randint

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='media/users/', verbose_name='аватар', **NULLABLE)
    phone = models.IntegerField(verbose_name='Номер телефона',  **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна',  **NULLABLE)
    email_verify = models.BooleanField(default=False, verbose_name='подтверждение почты')
    key = models.CharField(max_length=4, default=randint(1000, 9999), verbose_name='ключ регистрации')

    USERNAME_FIELD ="email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return (f'{self.email} {self.phone} {self.country}')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'