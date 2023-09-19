from django.shortcuts import render

from django.http import HttpResponse

from catalog.models import Category, Product


# def home(request):
#     print(request.GET)
#     return HttpResponse('OK')

def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name} ({email})')
    return render(request, 'catalog/contacts.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/categories.html', context)


def products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Продукты - {category_item.name}'
    }
    return render(request, 'catalog/products.html', context)
