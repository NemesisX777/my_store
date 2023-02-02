from rest_framework import generics
from products.models import Products, ProductCategory
from .serializers import ProductSerializer, CategorySerializer


class CategoriesAPIList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
