from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fellows, name="fellows"),
    path('destinations/', views.destinations, name="destinations"),
    path('companions/', views.companions, name="companions"),
    path('authorization/', views.auth, name="authorization"),
    path('authorize_user/', views.auth, name="authorize")
]
