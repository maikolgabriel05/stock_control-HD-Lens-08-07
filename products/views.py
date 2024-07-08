# products/views.py
from django.shortcuts import render, redirect
from products.forms import ProductsForm
from django.http import JsonResponse
from django.views import View
from products.models import Products


class ProductsListView(View):
    def get(self, request, *args, **kwargs):
        products = Products.objects.all()
        data = [
            {'pk': product.pk, 'name': product.name, 'stock': product.stock, 'price': product.price}
            for product in products
        ]
        return JsonResponse(data, safe=False)

def products(request):
    template_name = 'products.html'
    products = Products.objects.all()
    context = {'products': products}
    return render(request, template_name=template_name, context=context)


def create_product(request):
    template_name = 'create_product.html'
    form = ProductsForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('products:products')
        else:
            print(form.errors)

    return render(request, template_name=template_name, context=context)


def edit_product(request, pk):
    product = Products.objects.get(pk=pk)
    form = ProductsForm(request.POST or None, instance=product)
    template_name = 'edit_product.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('products:products')
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, template_name=template_name, context=context)


def delete_products(request, pk):
    product = Products.objects.get(pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('products:products')

    return render(request, 'delete_product.html', {'product': product})
