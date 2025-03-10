from django.shortcuts import render

from menu.models import Products


# Create your views here.

def catalog(request):

    menu = Products.objects.all()

    context = {
        'title': 'Меню',
        'menu': menu,
    }

    return render(request, 'menu/catalog.html', context)


def product(request):
    return render(request, 'menu/product.html')
