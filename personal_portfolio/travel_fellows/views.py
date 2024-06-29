from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import AuthorizeForm, RegisterForm
from .models import User


def destinations(request):
    return render(request, "travel_fellows/form.html")


def companions(request):
    return render(request, "travel_fellows/catalog.html")


def fellows(request):
    return render(request, "travel_fellows/main-page.html")


def auth(request):
    form = RegisterForm(request.POST)
    return render(request, "travel_fellows/register.html", {"form": form, "login": False})

class AuthorizeUser(View):
    def post(self, request):
        form = AuthorizeForm()
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        if form.is_valid():
            if password == 'correct_password':
                return HttpResponse('User authorized successfully!')
            else:
                return HttpResponse(f'<h1>USER WANT TO AUTHORIZE {password} {email}</h1>')
        else:
            return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors})

    def get(self, request):
        form = AuthorizeForm()
        return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors})


class RegisterUser(View):
    def get(self, request):
        form = AuthorizeForm()
        return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            password_confirm = form.cleaned_data['password']
            password = form.cleaned_data['password_confirm']
            email = form.cleaned_data['email']
            if password == password_confirm:
                user = User(name=form.cleaned_data['name'], surname=form.cleaned_data['surname'], email=email,
                            password=password)
                user.save()
                return HttpResponse('User registered successfully!')
            else:
                return HttpResponse(f'Registration went wrong')
        else:
            return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors})
