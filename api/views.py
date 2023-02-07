from rest_framework import generics
from products.models import Products, ProductCategory
from .serializers import ProductSerializer, CategorySerializer


# Define a generic view class that returns a serialized product list
class CategoriesAPIList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer


# Define a generic view class that returns a serialized category list
class ProductAPIList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


# Define a generic view class that returns a serialized list of products by category id
class CategoryDetail(generics.RetrieveAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer


class ProductsAPIListForCategory(generics.ListAPIView):
    # Specifies the serializer class to use for serializing the products queryset
    serializer_class = ProductSerializer

    def get_queryset(self):
        # Extracts the category id from the URL parameters
        category_id = self.kwargs.get('category_id')
        # Filters the products queryset based on the category id
        return Products.objects.filter(category__id=category_id)
