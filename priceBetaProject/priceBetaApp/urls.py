from django.urls import path
from .views import Product

urlpatterns = [
    path('', Product),
]