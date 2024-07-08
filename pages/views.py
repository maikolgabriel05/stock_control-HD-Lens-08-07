from django.shortcuts import render

from products.models import Products
from customers.models import Customers


def index(request):
    template_html = 'index.html'
    products = Products.objects.all().count()
    customers = Customers.objects.all().count()

    return render(request, template_html, context={
        'products': products, 'customers': customers}
                 )
