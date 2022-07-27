from django.urls import path
from . import views

urlpatterns = [
	path('index', views.index, name = "index"),
#	path('settings', views.settings, name='settings'),
#	path('signup/', views.signup, name = "signup"),
#	path('signin/', views.signin, name = "signin"),
#    path('signout/', views.signout, name = "signout")
]