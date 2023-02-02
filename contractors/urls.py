from django.urls import path

from contractors.views import ContractorList

urlpatterns = [
    path('', ContractorList.as_view(), name='contractor_list_url'),
]
