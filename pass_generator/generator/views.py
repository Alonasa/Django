from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    return render(request, 'generator/password.html')
