from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    strength = int(request.GET['length'])
    if request.GET.get('numbers'):
        ALPHABET.extend(list('0123456789'))
    if request.GET.get('special'):
        ALPHABET.extend(list('!@#$%^&*()_+'))
    if request.GET.get('upper'):
        ALPHABET.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


    for i in range(strength):
        thepassword += random.choice(ALPHABET)

    passw = ''.join(random.sample(thepassword, len(thepassword)))
    return render(request, 'generator/password.html', {'password':passw})
