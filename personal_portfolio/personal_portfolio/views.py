from django.shortcuts import render
from django.http.response import HttpResponse


def view(request):
    return HttpResponse("Simple view")
