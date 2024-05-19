from django.shortcuts import render
from django.http.response import HttpResponse


def view(request):
    return HttpResponse("Home page view")


def dynamic(request, num1, num2):
    add_res = num1 + num2
    result = f"{num1}+{num2} = {add_res}"
    return HttpResponse(str(result))
