from django.urls import path
from .views import Product, Category, Wishlist, Store

urlpatterns = [
    path('', Product),
    path('', Category),
    path('', Store),
    path('', Wishlist)
]