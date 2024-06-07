from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("I am main portfolio")


menu = {
    "/": "Travel Fellows",
    "about": "About",
    "fellows": "Fellows",
}


def fellows(request):
    return render(request, "travel_fellows/main-page.html")


def generator(request):
    return render(request, "generator/home.html")
