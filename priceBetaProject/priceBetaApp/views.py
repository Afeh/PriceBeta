from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# from priceBetaApp.forms import SignUpForm

























def index(request):
     user = request.user
     return render(request, 'index.html')



# def signup(request):
#     # if request.user.is_authenticated():
#     #     return redirect('index.html')
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index.html')
#         else:
#             form = SignUpForm()
#             return render(request, 'signup.html', {'form': form})
#     else:
#         form = SignUpForm()
#         return render(request, 'signup.html', {'form': form})