from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render
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
    # if request.method == 'POST':
    #     print("POST")
    #
    #     form = AuthorizeForm(request.POST, data=request.POST)
    #     if form.is_valid():
    #         password = form.cleaned_data['password']
    #         email = form.cleaned_data['username']
    #         user = authenticate(request, username=email, password=password)
    #         print(user)
    #         if user is not None:
    #             login(request, user)
    #             print("TRY AUTH TRUE")
    #             return HttpResponse("USER Logged In")
    #         else:
    #             return HttpResponse("USER NOT Logged")
    # else:
    #     print("GET")
    form = AuthorizeForm()

    return render(request, "travel_fellows/register.html",
                  {"form": form, "form-errors": form.errors, "form_address": reverse_lazy('auth-user'), "login": True})


class AuthorizeUser(View):
    def get(self, request):
        print("GET AUTH")
        form = AuthorizeForm()
        return render(request, "travel_fellows/register.html",
                      {"form": form, "form_errors": form.errors, "form_address": reverse_lazy('auth-user')})

    def post(self, request):
        form = AuthorizeForm(request.POST)
        print("AUTHO POST")
        print(form.is_valid())
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['username']
            username = User.objects.get(username=email).username
            user, created = User.objects.get_or_create(username=username, password=password)
            user_authenticated = authenticate(username=username, password=password, backend='personal_portfolio.authentication.EmailAuthBackend')
            if created:
                print("AUTH CREATED")
                login(request, user, backend='personal_portfolio.authentication.EmailAuthBackend')

            print(f"print{user}")
            print(user_authenticated is not None)
            print(f"{user} ITS A USER")
            if user_authenticated:
                login(request, user, backend='personal_portfolio.authentication.EmailAuthBackend')
                print("TRY AUTHORIZE TRUE")
                return HttpResponse("USER Logged In")
            return HttpResponse(f"USER NOT Logged, WRONG DATA AUTHUSER {form.errors}")
        return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors, "login": True,
                                                                "form_address": reverse_lazy("auth-user")})


class RegisterUser(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "travel_fellows/register.html",
                      {"form": form, "form_errors": form.errors, "form_address": reverse_lazy("register"),
                       "login": False})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            password_confirm = form.cleaned_data['password']
            password = form.cleaned_data['password_confirm']
            email = form.cleaned_data['username']
            if password == password_confirm:
                user = User.objects.create_user(name=form.cleaned_data['name'], surname=form.cleaned_data['surname'],
                                           username=email,
                                           password=password)
                user.save()
                return HttpResponse('User registered successfully!')
            else:
                return HttpResponse(f'Registration went wrong')
        else:
            return render(request, "travel_fellows/register.html",
                          {"form": form, "form_errors": form.errors, "form_address": reverse_lazy("register"),
                           "login": False})
