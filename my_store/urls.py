from django.contrib import admin
from django.urls import path, include

from my_store.views import redirect_root

urlpatterns = [
    path('', redirect_root, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('products/', include('products.urls')),
    path('contractors/', include('contractors.urls')),
    path('operations/', include('operations.urls')),
    path('api/', include('api.urls')),
]
