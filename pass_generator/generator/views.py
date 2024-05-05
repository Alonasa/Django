from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = []
    strength = 10
    for x in range(strength):
        thepassword.append(random.choice(ALPHABET))
    for i in range(int(strength/2)):
        el = random.choice(thepassword)
        idx = thepassword.index(el)
        thepassword[idx] = el.upper()

    password = ''.join(random.sample(thepassword, len(thepassword)))
    return render(request, 'generator/password.html', {'password':password})
