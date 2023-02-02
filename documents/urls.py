from django.urls import path

from .views import DemandList

urlpatterns = [
    path('', DemandList.as_view(), name='document_list_url'),
]
