from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from realapp import views

urlpatterns = [
    path('signup/', views.register,name='register'),
    path('login/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
     path('accounts/profile/',views.dashboard, name='dashboard'),# Built-in authentication URLs
    path('', views.home, name='home'),
    ]
