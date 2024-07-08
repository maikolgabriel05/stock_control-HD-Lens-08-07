# serializers.py
from rest_framework import serializers
from customers.models import Customers
from shopping.models import Shop, Products, CartItem, Sale


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['pk', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    shop = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all(), required=False)

    class Meta:
        model = CartItem
        fields = ['product', 'stock', 'price', 'shop']


class ShopSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customers.objects.all())
    itens = CartItemSerializer(many=True)

    class Meta:
        model = Shop
        fields = ['customer', 'itens']

    def create(self, validated_data):
        print("Dados validados recebidos no create:", validated_data)
        customer_id = validated_data.pop('customer').id
        itens_data = validated_data.pop('itens')

        shop = Shop.objects.create(customer_id=customer_id)

        for item_data in itens_data:
            print("Dados do item:", item_data)
            product_id = item_data.pop('product').id
            product = Products.objects.get(pk=product_id)
            CartItem.objects.create(shop=shop, product=product, **item_data)

        return shop


class SaleSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())

    class Meta:
        model = Sale
        fields = ['product', 'stock', 'price']

class SaleCreateSerializer(serializers.Serializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customers.objects.all())
    itens = SaleSerializer(many=True)

    def create(self, validated_data):
        customer = validated_data['customer']
        itens_data = validated_data['itens']
        sales = []
        for item_data in itens_data:
            sale = Sale.objects.create(customer=customer, **item_data)
            sales.append(sale)
        return sales