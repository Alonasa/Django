from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    return HttpResponse("I am main portfolio")


menu = {
    "/": "Travel Fellows",
    "about": "About",
    "fellows": "Fellows",
}


def fellows(request):
    return render(request, "travel_fellows/main-page.html", {"menu": menu})
