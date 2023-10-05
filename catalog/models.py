from django.db import models


NULLEBLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to= 'image_product/', verbose_name='изображение', **NULLEBLE)
    category = models.CharField(max_length=150, verbose_name='категория')
    purchase_price = models.PositiveIntegerField(verbose_name='цена покупки')
    date_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_last_modification = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}, {self.description}, {self.date_last_modification}'

    class Meta:
        verbose_name = 'наименование продукта'
        verbose_name_plural = 'наименования продуктов'
        ordering = ('name', )

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(max_length=1000, verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'наименование категории'
        verbose_name_plural = 'наименования категорий'
        ordering = ('name', )
