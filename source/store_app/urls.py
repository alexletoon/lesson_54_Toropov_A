from store_app.views.products import products_view, display_product, product_add_view
from store_app.views.category import category_add_view
from django.urls import path



urlpatterns = [
    path("", products_view, name ='index_view'),
    path("product/<int:pk>", display_product, name='product_view'),
    path('product/', products_view),
    path('product/add', product_add_view, name='add_product'),
    path('category/add', category_add_view, name='add_category' )
]