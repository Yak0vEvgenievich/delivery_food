from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from menu.models import Products


# Create your views here.

def catalog(request, category_slug, page =1):

    if category_slug == 'all':
        menu = Products.objects.all()
    else:
        menu = get_list_or_404(Products.objects.filter(category__slug= category_slug))

    paginator = Paginator(menu, 6)
    current_page = paginator.page(page)




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

    return render(request, 'menu/product.html', context= context)
