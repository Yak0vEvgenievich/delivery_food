from django.http import HttpResponse
from django.shortcuts import render
from menu.models import Categories

# Create your views here.

def index(request):


    context = {
        'title': 'Rolls Rice - главная',
        'content': 'Доставка роллов Rolls Rice',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Rolls Rice - о нас',
        'content': 'О нас',
        'text_on_page': "Текст о том о сем почему мы такие пиздатые",
    }

    return render(request, 'main/about.html', context)