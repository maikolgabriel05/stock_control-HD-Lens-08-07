from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from core import settings
from customers.views import CustomersListView
from products.views import ProductsListView
from shopping.views import shopping, cart_items, ShopCreateView, ProductListCreate, CartItemListCreate, CustomersListView
from . import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dashboard/', include('pages.urls')),
    path('dashboard/customer/', include('customers.urls')),
    path('dashboard/products/', include('products.urls')),
    path('shopping/', include('shopping.urls', namespace='shopping')),

    path('api/products/', ProductsListView.as_view(), name='product-list-create'),
    path('api/cart_items/', CartItemListCreate.as_view(), name='cartitem-list-create'),
    path('api/customers/', CustomersListView.as_view(), name='customers-list'),

    # API URLs
    path('api/', include([
        path('customers/', CustomersListView.as_view(), name='customer_list_api'),
        path('products/', ProductsListView.as_view(), name='products_list_api'),
        path('api-product/', v.api_product, name='api_product'),
        path('shopping-items/add/', v.api_shopping_items_add, name='api_shopping_items_add'),
        path('v1/', include('api.urls')),
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
        path('v1/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ])),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
