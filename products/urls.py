from django.urls import path

from products.views import ProductsList, ProductCategoryList

urlpatterns = [
    path('all-products/', ProductsList.as_view(), name='all_products_url'),
    path('categories/', ProductCategoryList.as_view(), name='all_categories_url'),
]
