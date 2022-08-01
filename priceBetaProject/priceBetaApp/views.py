from django.shortcuts import render, HttpResponse 

# Create your views here.

def Product(request):
    return HttpResponse("It is working")

def Category(request):
    return HttpResponse('Working')

def Store(request):
    return HttpResponse('Working')

def Wishlist(request):
    return HttpResponse('Working')