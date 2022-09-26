from store_app.views.products import products_view, display_product
from django.urls import path



urlpatterns = [
    path("", products_view),
    path("product/<int:pk>", display_product)
]