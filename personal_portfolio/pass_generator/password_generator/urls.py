from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mypassword/', views.password, name='password'),
    path('about/', views.about, name='about'),
]
