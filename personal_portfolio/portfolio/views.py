from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    return HttpResponse("I am main portfolio")


def fellows(request):
    return render(request, "travel_fellows/base.html")
