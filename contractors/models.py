from django.db import models


# Create your models here.

class ContractorCategory(models.Model):
    name = models.CharField('Категория', max_length=255, blank=False, null=False, default='Категория по умолчанию')
    is_active = models.BooleanField('Активный', default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория контрагента'
        verbose_name_plural = 'Категории контрагента'


class Contractor(models.Model):
    name = models.CharField('Наименование', max_length=255, blank=False, null=False)
    phone = models.CharField('Телефон', max_length=255, blank=True, null=True, default=None)
    email = models.EmailField('Почта', blank=True, null=True, default=None)
    address = models.TextField('Адрес', blank=True, null=True, default=None)
    is_active = models.BooleanField('Активный', default=True)
    category = models.ForeignKey(ContractorCategory, blank=True, null=True, default='Категория по умолчанию', on_delete=models.RESTRICT, verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class ContractorsObject(models.Model):
    name = models.CharField('Наименование', max_length=255, blank=True, null=True, default='Объект не указан')
    contractor = models.ForeignKey(Contractor, blank=True, null=True, default=None, on_delete=models.RESTRICT, verbose_name='Контрагент')
    is_active = models.BooleanField('Активный', default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
