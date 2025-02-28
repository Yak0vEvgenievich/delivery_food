from django.shortcuts import render


# Create your views here.

def catalog(request):
    context = {
        'title': 'Меню',
        'goods': [
            {'image': 'deps/images/goods/sushiset.jpeg',
             'name': 'Сет из суши',
             'description': 'Комплект из различных видов суши для наслаждения вкусом морепродуктов.',
             'price': 150.00},

            {'image': 'deps/images/goods/roll_salmon.jpeg',
             'name': 'Роллы с лососем',
             'description': 'Набор роллов с нежным лососем и авокадо, идеален для любителей рыбы.',
             'price': 93.00},

            {'image': 'deps/images/goods/roll_tunec.jpeg',
             'name': 'Острые роллы с тунцом',
             'description': 'Роллы с тунцом и острым соусом, для тех, кто любит пикантные блюда.',
             'price': 670.00},

            {'image': 'deps/images/goods/roll_fila.jpeg',
             'name': 'Роллы Филадельфия',
             'description': 'Классические роллы Филадельфия с крем-сыром и огурцом.',
             'price': 365.00},

            {'image': 'deps/images/goods/roll_tempura.jpeg',
             'name': 'Роллы Темпура',
             'description': 'Роллы с хрустящей темпурой и овощами, отличный выбор для гурманов.',
             'price': 430.00},

            {'image': 'deps/images/goods/roll_dragon.jpeg',
             'name': 'Дракон Ролл',
             'description': 'Уникальные роллы с угрем и авокадо, настоящая находка для любителей экзотики!',
             'price': 610.00},

            {'image': 'deps/images/goods/roll_ovoshi.jpeg',
             'name': 'Овощные роллы',
             'description': 'Легкие овощные роллы, идеальны для вегетарианцев.',
             'price': 55.00},

            {'image': 'deps/images/goods/roll_crab.jpeg',
             'name': 'Роллы с крабом',
             'description': 'Роллы с крабом и огурцом, для истинных ценителей морепродуктов.',
             'price': 190.00},

            {'image': 'deps/images/goods/roll_spicyshrimp.jpeg',
             'name': 'Острые роллы с креветками',
             'description': 'Роллы с креветками и острым соусом, вкус, который не оставит вас равнодушным.',
             'price': 30.00},

            {'image': 'deps/images/goods/roll_vegan.jpeg',
             'name': 'Веганские роллы',
             'description': 'Веганские роллы с авокадо и огурцом, свежий и полезный выбор.',
             'price': 10.00},

            {'image': 'deps/images/goods/roll_flavor.jpeg',
             'name': 'Цветочные роллы',
             'description': 'Дизайнерские роллы, украшенные съедобными цветами для красивой подачи.',
             'price': 15.00},

            {'image': 'deps/images/goods/roll_ananas.jpeg',
             'name': 'Роллы с ананасом',
             'description': 'Роллы необычной формы, но с отличным вкусом, подойдут для любителей экспериментов.',
             'price': 25.00},
        ]
    }

    return render(request, 'menu/catalog.html', context)


def product(request):
    return render(request, 'menu/product.html')
