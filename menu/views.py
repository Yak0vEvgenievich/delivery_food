from django.shortcuts import render, get_list_or_404


from menu.models import Products


# Create your views here.

def catalog(request, category_slug):

    if category_slug == 'all':
        menu = Products.objects.all()
    else:
        menu = get_list_or_404(Products.objects.filter(category__slug= category_slug))




    context = {
        'title': 'Меню',
        'menu': menu,
    }

    return render(request, 'menu/catalog.html', context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'menu/product.html', context= context)
