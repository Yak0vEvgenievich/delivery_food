from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from menu.models import Products

from menu.utils import q_search


# Create your views here.

def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        menu = Products.objects.all()
    elif query:
        menu = q_search(query)
    else:
        menu = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if order_by and order_by != 'default':
        menu = menu.order_by(order_by)

    paginator = Paginator(menu, 6)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Меню',
        'menu': current_page,
        'slug_url': category_slug
    }

    return render(request, 'menu/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'menu/product.html', context=context)
