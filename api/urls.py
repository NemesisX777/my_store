from django.urls import path

from .views import ProductAPIList, CategoriesAPIList, CategoryDetail, ProductsAPIListForCategory

urlpatterns = [
    path('products/', ProductAPIList.as_view(), name='api_all_products_url'),
    path('categories/', CategoriesAPIList.as_view(), name='api_all_categories_url'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('categories/<int:category_id>/products/', ProductsAPIListForCategory.as_view(), name='products_for_category'),
    ]
