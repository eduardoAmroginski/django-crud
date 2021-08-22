from django.urls import path
from products.views import create_product, delete_product, list_products, update_product


urlpatterns = [
    path('', list_products, name='list_products'), #READ
    path('new', create_product, name='create_products'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
    
]


# CRUD - CREATE, READ, UPDATE, DELETE