from django.shortcuts import render


def destinations(request):
    return render(request, "travel_fellows/form.html")


def companions(request):
    return render(request, "travel_fellows/catalog.html")


def fellows(request):
    return render(request, "travel_fellows/main-page.html")


def auth(request):
    return render(request, "travel_fellows/register.html")


def authorize_user(request):
    if request.POST:
        return f'<h1>USER WANT TO AUTHORIZE {request["password"]}</h1>'
