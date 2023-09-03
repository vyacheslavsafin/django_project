from django.shortcuts import render

from django.http import HttpResponse


# def home(request):
#     print(request.GET)
#     return HttpResponse('OK')

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name} ({email})')
    return render(request, 'catalog/contacts.html')
