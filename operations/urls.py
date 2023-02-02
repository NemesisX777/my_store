from django.urls import path

from operations.views import ClientPaymentOrderList

urlpatterns = [
    path('', ClientPaymentOrderList.as_view(), name='client_payment_list_url'),
]
