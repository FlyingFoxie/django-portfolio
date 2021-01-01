from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileListView

urlpatterns = [
	path('', ProfileListView.as_view(), name='dashboard'),
    path('register/', views.registerPage, name='register'),
    path('settings/',views.profileSettings, name='profile'),
    path('login/', views.login, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	path('profileview/<str:pk>', views.profileview, name='preview'),
]
