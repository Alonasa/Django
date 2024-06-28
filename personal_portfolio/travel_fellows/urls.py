from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fellows, name="fellows"),
    path('destinations/', views.destinations, name="destinations"),
    path('companions/', views.companions, name="companions"),
    path('auth/', views.auth, name="authorize"),
    path('auth-form/', views.register_user, name="auth-user"),
    path('register-form/', views.register_user, name="register"),
]
