from datetime import date

from django.db import models

from contractors import models as contractors_models
from products import models as products_models


class Demand(models.Model):  # Модель заявки
    STATE_CHOICES = (
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('ordered', 'Размещена у поставщика'),
        ('on_store', 'Получена от поставщика'),
        ('delivered', 'Доставлена клиенту'),
        ('paid', 'Оплачена'),
        ('done', 'Закрыта'),
    )
    date = models.DateField('Дата', default=date.today)  # Дата заявки
    obj = models.ForeignKey(contractors_models.ContractorsObject, on_delete=models.RESTRICT,
                            verbose_name='Объект')  # Объект заявки
    product_list = models.ManyToManyField(products_models.Products, verbose_name='Товары')  # Товары заявки
    state = models.CharField(max_length=255, choices=STATE_CHOICES, verbose_name='Статус',
                             default='Новая')  # Статус заявки

    def __str__(self):
        return f'Заявка №{self.id} от {self.date}. Объект: {self.obj}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Invoice(models.Model):  # Модель счета
    date = models.DateField('Дата', default=date.today)  # Дата и время создания счета
    obj = models.ForeignKey(contractors_models.ContractorsObject, on_delete=models.RESTRICT,
                            verbose_name='Объект')  # Объект счета
    product_list = models.ManyToManyField(products_models.Products, verbose_name='Товары')  # Товары счета
    is_handed = models.BooleanField(verbose_name='Выставлен клиенту', default=False)  # Выставлен клиенту
    is_paid = models.BooleanField(default=False, verbose_name='Оплачен')  # Оплачен ли счет

    # sum_of_invoice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма счета', default=0)

    @property
    def full_sum_of_invoice(self):
        return sum([product.price for product in self.product_list.all()])

    def __str__(self):
        return f'Счет №{self.id} от {self.date}'

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
