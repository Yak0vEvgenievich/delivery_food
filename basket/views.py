from django.shortcuts import render, redirect
from menu.models import Products
from basket.models import Basket


# Create your views here.
def basket_add(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user, product=product)

        if basket.exists():
            basket = basket.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
            Basket.objects.create(user=request.user, product= product, quantity = 1)

    # альтернатива return redirect('products:list')
    return redirect(request.META['HTTP_REFERER'])

def basket_change(request, product_slug):
    pass


def basket_remove(request, product_slug):
    pass
