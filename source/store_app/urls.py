from store_app import views
from django.urls import path



urlpatterns = [
    path("", views.products_view)
]