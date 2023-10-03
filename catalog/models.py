from django.db import models


NULLEBLE = {'blank': True, 'null': True}


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='наименование')
    description_product = models.TextField(max_length=1000, verbose_name='описание')
    image_product = models.ImageField(upload_to= 'image_product/', verbose_name='изображение', **NULLEBLE)
    category_product = models.CharField(max_length=150, verbose_name='категория')
    purchase_price_product = models.IntegerField(verbose_name='цена покупки')
    date_creation_product = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_last_modification_product = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name_product}, {self.description_product}, {self.date_last_modification_product}'

    class Meta:
        verbose_name = 'наименование продукта'
        verbose_name_plural = 'наименования продуктов'
        ordering = ('name_product', )

class Category(models.Model):
    name_category = models.CharField(max_length=150, verbose_name='наименование')
    description_category = models.TextField(max_length=1000, verbose_name='описание')

    def __str__(self):
        return f'{self.name_category}, {self.description_category}'

    class Meta:
        verbose_name = 'наименование категории'
        verbose_name_plural = 'наименования категорий'
        ordering = ('name_category', )
