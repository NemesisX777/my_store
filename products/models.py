from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField('Наименование', max_length=255, blank=False, null=False, default='Категория по умолчанию')
    is_active = models.BooleanField('Активный', default=True)
    parent = models.ForeignKey('self', blank=True, null=True, default='Категория по умолчанию',
                               on_delete=models.SET_DEFAULT, verbose_name='Родительская категория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'


class Products(models.Model):
    name = models.CharField('Наименование', max_length=255, blank=True, null=True, default=None)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2, default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.RESTRICT,
                                 verbose_name='Категория товара')
    is_active = models.BooleanField('Активный', default=True)

    def __str__(self):
        return f'{self.name} - {self.price} руб.'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
