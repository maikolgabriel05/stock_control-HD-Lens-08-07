# products/urls.py
from django.urls import path
from .views import ProductsListView, products, create_product, edit_product, delete_products

app_name = 'products'

urlpatterns = [
    path('api/products/', ProductsListView.as_view(), name='products_list_api'),
    path('list-products/', products, name='products'),
    path('create-product/', create_product, name='create_product'),
    path('edit-product/<int:pk>/', edit_product, name='edit_product'),
    path('delete-product/<int:pk>/', delete_products, name='delete_products'),
]
