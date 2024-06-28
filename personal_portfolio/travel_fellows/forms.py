from wsgiref import validate
from django import forms
from django.core import validators
from django.core.validators import EmailValidator


class AuthorizeForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(
            attrs={'id': 'email', 'class': 'registration__email', 'name': 'email', 'placeholder': 'E-mail'}),
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'id': 'password', 'class': 'registration__password', 'type': 'password', 'name': 'password',
                   'placeholder': 'Password'}),
        min_length=8
    )

