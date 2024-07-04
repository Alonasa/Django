from django.contrib.auth import authenticate, login, aauthenticate, alogin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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
    if request.method == 'GET':
        form = AuthorizeForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                print("TRY AUTH TRUE")
                return HttpResponse("USER Logged In")
            else:
                return HttpResponse("USER NOT Logged")
    else:
        form = AuthorizeForm()

    return render(request, "travel_fellows/register.html", {"form": form, "form_address": reverse_lazy('auth-user'), "login": True})


class AuthorizeUser(View):
    def get(self, request):
        form = AuthorizeForm()
        return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors, "form_address": reverse_lazy('auth-user')})

    def post(self, request):
        form = AuthorizeForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = authenticate(request, username=email, password=password)
            print(user)
            print(user is not None)
            if user is not None:
                login(request, user)
                print("TRY AUTHORIZE TRUE")
                return HttpResponse("USER Logged In")
            else:
                return HttpResponse("USER NOT Logged, WRONG DATA AUTHUSER")
        else:
            return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors, "login": True, "form_address": reverse_lazy("auth-user")})


class RegisterUser(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors, "form_address": reverse_lazy("register"), "login": False})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            password_confirm = form.cleaned_data['password']
            password = form.cleaned_data['password_confirm']
            email = form.cleaned_data['email']
            if password == password_confirm:
                user = User.objects.create(name=form.cleaned_data['name'], surname=form.cleaned_data['surname'], email=email,
                            password=password)
                user.save()
                return HttpResponse('User registered successfully!')
            else:
                return HttpResponse(f'Registration went wrong')
        else:
            return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors, "form_address": reverse_lazy("register"),  "login": False})
