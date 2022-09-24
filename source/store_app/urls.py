from store_app.views.products import products_view
from django.urls import path



urlpatterns = [
    path("", products_view)
]