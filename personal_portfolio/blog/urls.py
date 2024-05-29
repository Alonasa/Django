from django.urls import path,include
from django.http.response import HttpResponse
from . import views


def home(request):
    return HttpResponse("Blog Home page")


urlpatterns = [
    path('', views.blog_main, name='blog'),
]

