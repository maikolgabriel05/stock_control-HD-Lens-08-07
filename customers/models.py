# customers/models.py
from django.db import models


class Customers(models.Model):
    name = models.CharField(verbose_name='Cliente', max_length=150, null=False, blank=False)
    cnpj = models.CharField(verbose_name='CNPJ', max_length=14, null=False, blank=False, unique=True)
    email = models.EmailField(verbose_name='Email ', unique=True)
    state = models.CharField(verbose_name='Estado', max_length=20, null=True)
    city = models.CharField(verbose_name='Cidade', max_length=100, null=True)
    address = models.CharField(verbose_name='Endereço', max_length=100, null=True)
    create_by = models.DateField(auto_now_add=True)



    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
        db_table = 'customers_customer'

    def __str__(self):
        return self.name
