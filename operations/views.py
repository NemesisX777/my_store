from django.views.generic import ListView

from operations.models import ClientPaymentOrder


class ClientPaymentOrderList(ListView):
    model = ClientPaymentOrder
    context_object_name = 'client_payment_orders'
    template_name = 'operations/client_payment_order_list.html'
