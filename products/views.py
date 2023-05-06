from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    context = {'title': 'Ruffle',
               'is_promotion': False}
    return render(request=request, template_name='products/index.html', context=context)


def products(request):
    context = {'title': 'Ruffle',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()
               }
    return render(request=request, template_name='products/products.html', context=context)
