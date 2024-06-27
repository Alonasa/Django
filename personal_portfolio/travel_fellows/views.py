from django.http import HttpResponse
from django.shortcuts import render

from .forms import AuthorizeForm


def destinations(request):
    return render(request, "travel_fellows/form.html")


def companions(request):
    return render(request, "travel_fellows/catalog.html")


def fellows(request):
    return render(request, "travel_fellows/main-page.html")


def auth(request):
    form = AuthorizeForm(request.POST)
    return render(request, "travel_fellows/register.html", {"form": form})


def authorize_user(request):
    if request.method == 'POST':
        form = AuthorizeForm(request.POST)
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        if form.is_valid():
            if password == 'correct_password':
                return HttpResponse('User authorized successfully!')
            else:
                return HttpResponse(f'<h1>USER WANT TO AUTHORIZE {password} {email}</h1>')
        else:
            return render(request, "travel_fellows/register", context={"form": form})
    else:
        form = AuthorizeForm()
