from django.db import models
from customers.models import Customers
from products.models import Products


class Shop(models.Model):
    customer = models.ForeignKey(
        Customers,
        verbose_name='cliente',
        related_name='shops',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField('criado em', auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'compra'
        verbose_name_plural = 'compras'

    def __str__(self):
        return str(self.customer)


class CartItem(models.Model):
    shop = models.ForeignKey(
        Shop,
        related_name='compras',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Products,
        related_name='products',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    stock = models.PositiveIntegerField('quantidade')
    price = models.DecimalField('preço', max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'item do carrinho'
        verbose_name_plural = 'itens do carrinho'

    def __str__(self):
        if self.shop:
            return f'{self.shop.pk}-{self.pk}-{self.product}'
        return str(self.pk)

    def get_subtotal(self):
        return self.price * (self.stock or 0)


class Sale(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField('quantidade')
    price = models.DecimalField('preço', max_digits=6, decimal_places=2)

