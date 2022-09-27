from django.shortcuts import render, get_object_or_404, redirect, reverse
from store_app.models import Categories, Goods


def category_add_view(request):
    if request.method == 'GET':
        return render (request, 'add_category.html')
    else:
        category_info = {
            'category': request.POST.get('category'),
            'description': request.POST.get('description')
        }
    Categories.objects.create(**category_info)
    return redirect(reverse('index_view'))