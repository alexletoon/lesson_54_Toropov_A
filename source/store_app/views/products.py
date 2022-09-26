from django.shortcuts import render, get_object_or_404
from store_app.models import Categories, Goods


def products_view (request):
    products = Goods.objects.all()
    context = {
        'goods': products

    }   
    return render(request, 'index.html', context = context)


def display_product(request, pk):
    good = get_object_or_404(Goods, id = pk)
    return render(request, 'product.html', context = {
        'good': good
    })