from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная страница',
        'is_sale': False, #выводит сообщение на главной странице о том, что действует скидка
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Каталог'
    }
    return render(request, 'products/products.html', context)
