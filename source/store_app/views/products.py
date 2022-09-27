from django.shortcuts import render, get_object_or_404, redirect, reverse
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


def product_add_view(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'add_product.html', context=context)
    else:
        product_info = {
            'good': request.POST.get('good'),
            'category': request.POST.get('category'),
            'price': request.POST.get('price'),
            'pic': request.POST.get('pic'),
            'description': request.POST.get('description'),
        }
        category = Categories()
        category.id = request.POST.get('category')
        good = Goods.objects.create(good = product_info['good'], category=category, price = product_info['price'], pic = product_info['pic'], description = product_info['description'])
        return redirect(reverse('product_view', kwargs={'pk': good.id}))