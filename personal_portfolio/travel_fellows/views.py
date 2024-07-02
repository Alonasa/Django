import logging
import pdb

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    print("HELLO")
    if request.method == 'POST':
        form = AuthorizeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                return HttpResponse("USER Logged In")
            else:
                return redirect("auth-form")
    else:
        form = AuthorizeForm()

    return render(request, "travel_fellows/register.html", {"form": form, "login": True})


class AuthorizeUser(View):
    print("AUTH FUNC")

    def get(self, request):
        form = AuthorizeForm()
        return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors})

    def post(self, request):
        form = AuthorizeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email)

            user = authenticate(request, username=email, password=password)
            if user is not None:
                return HttpResponse("USER Logged In")
            else:
                return redirect("auth-form")
        else:
            return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors, "login": True})

class RegisterUser(View):
    print("CHECK REGISTER")
    def get(self, request):
        form = RegisterForm()
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
