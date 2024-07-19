from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from .forms import AuthorizeForm, RegisterForm, UserPhotoForm, UserHashtagsForm
from .models import User, UserProfile


def destinations(request):
    return render(request, "travel_fellows/form.html")


def companions(request):
    return render(request, "travel_fellows/catalog.html")


def fellows(request):
    return render(request, "travel_fellows/main-page.html")


def auth(request):
    form = AuthorizeForm()
    return render(request, "travel_fellows/register.html",
                  {"form": form, "form-errors": form.errors, "form_address": reverse_lazy('auth-user'), "login": True})


class AuthorizeUser(View):
    def get(self, request):
        form = AuthorizeForm()
        return render(request, "travel_fellows/register.html",
                      {"form": form, "form_errors": form.errors, "form_address": reverse_lazy('auth-user')})

    def post(self, request):
        form = AuthorizeForm(request.POST)
        backend = 'personal_portfolio.authentication.EmailAuthBackend'
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['username']
            username = User.objects.filter(username=email).first()
            if username is not None:
                user = authenticate(request, username=username, password=password,
                                    backend=backend)

                if user is not None:
                    login(request, user, backend=backend)
                    return redirect('fellows')
                return HttpResponse(f"USER NOT Logged, WRONG DATA AUTHUSER")
            else:
                return HttpResponse(f"WE DONT FIND SUCH USERNAME IN OUR DATABASE")

        return render(request, "travel_fellows/register.html", {"form": form, "form_errors": form.errors, "login": True,
                                                                "form_address": reverse_lazy("auth-user")})


def logOut(request):
    logout(request)
    return redirect('fellows')


@method_decorator(login_required, name='dispatch')
class ViewUserProfile(View):

    def get_context(self, form, user_profile, hashtags_form):
        context = {
            "form": form,
            "user": user_profile,
            "image": f"img/{user_profile.photo.url}",
            "textarea_form": hashtags_form
        }

        return context


    def get(self, request):
        form = UserPhotoForm()
        hashtags_form = UserHashtagsForm(request.POST)
        user_profile = UserProfile.objects.get(user=request.user)
        context = self.get_context(form, user_profile, hashtags_form)
        return render(request, "travel_fellows/form.html", context)

    def post(self, request):
        form = UserPhotoForm(request.POST, request.FILES)
        hashtags_form = UserHashtagsForm(request.POST)
        user_profile = UserProfile.objects.get(user=request.user)

        context = self.get_context(form, user_profile, hashtags_form)
        if form.is_valid():
            print(form.changed_data)
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                user_profile.hashtags = form.cleaned_data.get('hashtags', '')
                user_profile.save()
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(
                    user=request.user,
                    photo=request.FILES['user_photo']
                )

            context = self.get_context(form, user_profile)
            return render(request, "travel_fellows/form.html", context)

        return render(request, "travel_fellows/form.html", context)


class RegisterUser(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "travel_fellows/register.html",
                      {"form": form, "form_errors": form.errors, "form_address": reverse_lazy("register"),
                       "login": False})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            password_confirm = form.cleaned_data['password']
            password = form.cleaned_data['password_confirm']
            email = form.cleaned_data['username']
            if password == password_confirm:
                user = User.objects.create(name=name, surname=surname,
                                           username=email,
                                           password=password)
                user.set_password(password)
                user.save()
                return HttpResponse('User registered successfully!')
            else:
                return HttpResponse(f'Registration went wrong')
        else:
            return render(request, "travel_fellows/register.html",
                          {"form": form, "form_errors": form.errors, "form_address": reverse_lazy("register"),
                           "login": False})
