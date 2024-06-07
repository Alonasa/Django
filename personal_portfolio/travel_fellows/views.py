from django.shortcuts import render


def form(request):
    return render(request, "travel_fellows/form.html")


def fellows(request):
    return render(request, "travel_fellows/main-page.html")
