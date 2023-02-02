from django.contrib import admin
from .models import Purchase, PaymentOrder, ClientPaymentOrder, Shipment


admin.site.register(Purchase)
admin.site.register(PaymentOrder)
admin.site.register(ClientPaymentOrder)
admin.site.register(Shipment)
