from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect

from products.models import Product, ProductCategory, Basket


def index(request):
    context = {'title': 'Ruffle',
               'is_promotion': False}
    return render(request=request, template_name='products/index.html', context=context)


def products(request, category_id=None):
    per_page = 3
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    page = request.GET.get('page', 1)
    if not isinstance(page, int):
        if page.isdigit():
            page = int(page)
        else:
            page = 1
    paginator = Paginator(products, per_page=per_page)
    page_products = paginator.page(page)
    return render(request, 'products/products.html', context={
        'title': 'Ruffle продукты',
        'products': page_products,
        'category': ProductCategory.objects.all(),
        'category_id': category_id
    })



@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
