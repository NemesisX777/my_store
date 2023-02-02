from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from products.models import Products, ProductCategory


class ProductsList(ListView):
    model = Products
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = ['name']


class ProductCategoryList(ListView):
    model = ProductCategory
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    paginate_by = 5
    ordering = ['name']


def sample_view(request):
    return render(request, 'products/sample.html', {})
