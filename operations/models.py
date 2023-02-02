from django.db import models


class Purchase(models.Model):  # Модель закупки у поставщика
    date = models.DateField(auto_now_add=True)  # Дата и время создания закупки


class PaymentOrder(models.Model):  # Модель платежного поручения
    pass


class ClientPaymentOrder(models.Model):  # Модель оплаты от клиента
    pass


class Shipment(models.Model):  # Модель отгрузки
    pass
