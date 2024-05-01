from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def eggs(request):
    return HttpResponse("<h1>Eggs</h1>")