from django.shortcuts import render

from catalog.models import Product


def home(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        print(pk)

    product_list = Product.objects.all()
    context = {
        'products': product_list
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Получено сообщение: {name}, ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


def product(request):
    product = Product.objects.get(pk=3)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
