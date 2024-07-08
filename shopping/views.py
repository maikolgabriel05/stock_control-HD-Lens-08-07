# views.py
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Shop, CartItem
from products.models import Products
from customers.models import Customers
from serializers import ShopSerializer, ProductSerializer, CartItemSerializer, CustomerSerializer, SaleCreateSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


def shopping(request):
    template_name = 'shopping.html'
    return render(request, template_name)


def cart_items(request, pk):
    template_name = 'cart_items.html'
    carts = CartItem.objects.filter(shop=pk)

    if carts.exists():
        qs = carts.values_list('price', 'stock')
        total = sum(map(lambda q: q[0] * q[1], qs))
    else:
        total = 0

    context = {'object_list': carts, 'total': total}
    return render(request, template_name, context)


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class CartItemListCreate(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CustomersListView(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer


class ShopCreateView(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class SaleCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SaleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
