from django.urls import path

from .views import ProductAPIList, CategoriesAPIList

urlpatterns = [
    path('products/', ProductAPIList.as_view(), name='api_all_products_url'),
    path('categories/', CategoriesAPIList.as_view(), name='api_all_categories_url'),
]
