from django.shortcuts import render
from store_app.models import Categories, Goods


def products_view (request):
    products = Goods.objects.all()
    context = {
        'goods': products

    }   
    return render(request, 'index.html', context = context)