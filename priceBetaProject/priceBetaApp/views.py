from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def index(request):
     user = request.user
     return render(request, 'index.html')



