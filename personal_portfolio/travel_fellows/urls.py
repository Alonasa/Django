from django.urls import path
from . import views

urlpatterns = [
    path('', views.fellows, name="fellows"),
    path('form/', views.form, name="form")
]