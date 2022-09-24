from calendar import TUESDAY
from django.db import models

class Categories(models.Model):
    category = models.CharField(verbose_name="Категория", max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Описание категории', max_length=1000, null=True, blank = True)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата обновления', auto_now=True)

    def __str__(self) -> str:
        return f' Category -  {self.category}, description - {self.description}'



class Goods(models.Model):
    category = models.ForeignKey(verbose_name='Категория', to='store_app.Category', null=False, blank=False, related_name='products', on_delete=models.RESTRICT)
    good = models.CharField(verbose_name='Название продукта', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Описание продукта', max_length=3000, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    price = models.DecimalField(verbose_name='Цена', null=False, blank=False, max_digits=10, decimal_places=2)
    pic = models.URLField(verbose_name='Фото', blank=True, null=True, default='product_pic')


    def __str__(self) -> str:
        return f'Good - {self.good}, price - {self.price} '