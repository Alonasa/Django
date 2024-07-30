import calendar
import datetime

from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from .forms import AuthorizeForm, RegisterForm, UserPhotoForm, UserHashtagsForm, UserTransportationForm, UserPlans, \
    UserPlansForm, CalendarWidget
from .models import User, UserProfile, HashTag, UserTransportation


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

    def get_context(self, form, user_profile, hashtags_form, transportation_form, hashtags, plans_form, calendar):
        context = {
            "form": form,
            "user": user_profile,
            "image": f"img/{user_profile.photo.url}",
            "textarea_form": hashtags_form,
            "transportation_form": transportation_form,
            "hashtags": hashtags,
            "plans_form": plans_form,
            "calendar": calendar
        }

        return context

    def cal(self):
        cal = forms.DateField(widget=CalendarWidget)
        print(cal)
        return cal

    def get(self, request):
        form = UserPhotoForm()
        user_profile = UserProfile.objects.get(user=request.user)
        hashtags = request.user.hashtag_set.all()
        str_hashtags = ' '.join(f'{ha.hashtag}' for ha in hashtags)
        hashtags_form = UserHashtagsForm(initial={'hashtags': str_hashtags})
        user_transportation, created = UserTransportation.objects.get_or_create(user=request.user)
        transportation_form = UserTransportationForm(request.POST, instance=user_transportation)
        plans_form = UserPlansForm()
        context = self.get_context(form, user_profile, hashtags_form, transportation_form, str_hashtags, plans_form,
                                   self.cal())
        return render(request, "travel_fellows/form.html", context)

    def post(self, request):
        form = UserPhotoForm(request.POST, request.FILES)
        user_profile = UserProfile.objects.get(user=request.user)
        hashtags = request.user.hashtag_set.all()
        str_hashtags = ' '.join(f'{ha.hashtag}' for ha in hashtags)
        hashtags_form = UserHashtagsForm(request.POST, initial={'hashtags': str_hashtags})
        user_transportation, _ = UserTransportation.objects.get_or_create(user=request.user)
        transportation_form = UserTransportationForm(request.POST, instance=user_transportation)
        plans_form = UserPlansForm()
        context = self.get_context(form, user_profile, hashtags_form, transportation_form, str_hashtags, plans_form,
                                   self.cal())

        if form.is_valid():
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                user_profile.save()

                if hashtags_form.is_valid():
                    hashtags = hashtags_form.data.get('hashtags').strip().split(' ')
                    unique_hashtags = set(hashtags)

                    for tag in unique_hashtags:
                        if tag.startswith('#'):
                            try:
                                hash_tag = HashTag.objects.get(hashtag=tag.lower())
                            except HashTag.DoesNotExist:
                                hash_tag = HashTag.objects.create(hashtag=tag.lower())
                                user = request.user
                                user.hashtag_set.add(hash_tag)
                                user.save()
                            hash_tag.save()

                if transportation_form.is_valid():
                    transportation_form.save()

            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(
                    user=request.user,
                    photo=request.FILES['user_photo']
                )
                user_profile.save()

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
