from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.profile, name='home'),
    path('login/', views.login, name='login'),
	path('logout/', views.logoutUser, name='logout'),
]
