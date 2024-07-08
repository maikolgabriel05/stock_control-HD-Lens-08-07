# customers/urls.py
from django.urls import path
from .views import CustomersListView, customers_list, create_customer, edit_customer, delete_customer

app_name = 'customers'

urlpatterns = [
    path('api/customers/', CustomersListView.as_view(), name='customer_list_api'),
    path('list/', customers_list, name='customers_list'),
    path('create/', create_customer, name='create_customer'),
    path('edit/<int:pk>/', edit_customer, name='edit_customer'),
    path('delete/<int:pk>/', delete_customer, name='delete_customer'),
]
