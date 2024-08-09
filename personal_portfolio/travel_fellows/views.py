from datetime import datetime

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View

from .forms import AuthorizeForm, RegisterForm, UserPhotoForm, UserHashtagsForm, UserTransportationForm, UserPlansForm
from .models import User, UserProfile, HashTag, UserTransportation, UserPlans


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
    def get_context(self, form, user_profile, hashtags_form, transportation_form, hashtags, plans_form):
        hashtags = user_profile.user.hashtag_set.all()
        str_hashtags = ' '.join(f'{ha.hashtag}' for ha in hashtags)
        hashtags_form = UserHashtagsForm(initial={'hashtags': str_hashtags})

        context = {
            "form": form,
            "user": user_profile,
            "image": f"img/{user_profile.photo.url}",
            "textarea_form": hashtags_form,
            "transportation_form": transportation_form,
            "hashtags": hashtags,
            "plans_form": plans_form,
        }

        return context

    def get(self, request):
        form = UserPhotoForm()
        user_profile = UserProfile.objects.get(user=request.user)
        hashtags = request.user.hashtag_set.all()
        str_hashtags = ' '.join(f'{ha.hashtag}' for ha in hashtags)
        hashtags_form = UserHashtagsForm(initial={'hashtags': str_hashtags})
        transportation_form = UserTransportationForm(instance=UserTransportation.objects.get(user=request.user))
        plans_form = UserPlansForm(request.GET, prefix='plans')
        context = self.get_context(form, user_profile, hashtags_form, transportation_form, str_hashtags, plans_form)
        return render(request, "travel_fellows/form.html", context)

    def handle_photo_form(self, request, user_profile):
        form = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            if form.has_changed():
                user_profile.photo = request.FILES['user_photo']
                user_profile.save()
        return form

    def handle_hashtags_form(self, request, user):
        hashtags_form = UserHashtagsForm(request.POST, initial={
            'hashtags': ' '.join(user.hashtag_set.values_list('hashtag', flat=True))})
        if hashtags_form.is_valid():
            if hashtags_form.has_changed():
                print("HASHTAGS CHANED")
                hashtags = hashtags_form.cleaned_data.get('hashtags').strip().split()
                unique_hashtags = set(hashtags)
                for tag in unique_hashtags:
                    if tag.startswith('#'):
                        try:
                            hash_tag, _ = HashTag.objects.get_or_create(hashtag=tag.lower())
                            user.hashtag_set.add(hash_tag)
                        except HashTag.DoesNotExist:
                            pass
                user.save()
        return hashtags_form

    def handle_transportation_form(self, request, user):
        user_transportation, _ = UserTransportation.objects.get_or_create(user=user)
        transportation_form = UserTransportationForm(request.POST, instance=user_transportation)
        if transportation_form.is_valid():
            transportation_form.save()
        return transportation_form

    def handle_plans_form(self, request):
        plans_form = UserPlansForm(request.POST)
        if plans_form.is_valid():
            return plans_form

    def post(self, request):
        user = request.user
        user_profile, _ = UserProfile.objects.get_or_create(user=user)

        photo_form = self.handle_photo_form(request, user_profile)
        hashtags_form = self.handle_hashtags_form(request, user)
        plans_form = self.handle_plans_form(request)
        transportation_form = self.handle_transportation_form(request, user)

        context = self.get_context(
            photo_form, user_profile, hashtags_form, transportation_form,
            user.hashtag_set.values_list('hashtag', flat=True), plans_form
        )

        return render(request, "travel_fellows/form.html", context)


def handlePlans(request):
    if request.method == 'POST':
        form_data = dict(request.POST)
        print(form_data)
        cleaned_data = {}
        for key, value in form_data.items():
            if key == 'csrfmiddlewaretoken':
                cleaned_data[key] = value[0]
            elif key.endswith('-companions') or key.endswith('-length'):
                cleaned_data[key] = int(value[0])
            elif key == 'picked-date':
                cleaned_data[key] = [datetime.strptime(date, '%B-%d-%Y').date() for date in value]
            elif key == 'country-letter' or key == 'plans-kids':
                cleaned_data[key] = 'on' in value
            else:
                cleaned_data[key] = value[0]
        print(cleaned_data)

        user = request.user
        print(user.id)
        start_trip = cleaned_data['picked-date'][0]
        end_trip = cleaned_data['picked-date'][1]
        companions = cleaned_data['plans-companions']
        length = cleaned_data['plans-length']

        try:
            kids = cleaned_data['plans-kids']
        except KeyError:
            kids = False

        plans = [cleaned_data['plans']]

        UserPlans.objects.create(user=user, destinations=[], companions=companions, length=length, dates_start=start_trip,
                                 dates_end=end_trip, kids=kids, plans=plans)

        return redirect("user")


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
