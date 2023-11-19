# Generated by Django 4.2.6 on 2023-11-19 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(max_length=90, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('Content', models.CharField(max_length=300, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение (превью)')),
                ('date_of_creation', models.DateField(default=django.utils.timezone.now, verbose_name='дата создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('view_count', models.IntegerField(default=0, verbose_name='Счетчик просмотров')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
