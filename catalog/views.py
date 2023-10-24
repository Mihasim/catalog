from django.shortcuts import render

from catalog.models import Product


def home(request):
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


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    product_list = Product.objects.all()
    context = {
        'product_id': Product.objects.filter(id=pk),
        'title': f'Страница товара {product_item.name}',
        'product_data': product_list[pk]
    }
    return render(request, 'catalog/product.html', context)
