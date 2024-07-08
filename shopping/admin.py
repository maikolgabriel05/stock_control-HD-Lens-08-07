from django.contrib import admin
from .models import Shop, CartItem


class CartInline(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = (CartInline,)
    list_display = ('__str__', 'created')
    search_fields = ('customer',)


@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'shop', 'stock', 'price')
    search_fields = ('shop__customer', 'product__name')
