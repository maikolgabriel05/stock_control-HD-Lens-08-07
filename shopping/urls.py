from django.urls import path
from shopping import views as v
from .views import CartItemListCreate

app_name = 'shopping'

urlpatterns = [
    path('shopping/', v.shopping, name='shopping'),
    path('cart-items/<int:pk>/', v.cart_items, name='cart_items'),
    path('carts/', CartItemListCreate.as_view(), name='cartitem-list-create'),
]
