from django import forms
from django.forms import ModelForm
from .models import User, AuthUser


class BaseForm(ModelForm):
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(
            attrs={'id': 'email', 'class': 'registration__email', 'name': 'email', 'placeholder': 'E-mail'}),
        error_messages={"required": "*Required Field"}
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'id': 'password', 'class': 'registration__password', 'type': 'password', 'name': 'password',
                   'placeholder': 'Password'}),
        min_length=8,
        error_messages={"required": "*Required Field", "max_length": "Min password length is 8 Characters"}
    )


class AuthorizeForm(BaseForm):
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(
            attrs={'id': 'email', 'class': 'registration__email', 'name': 'email', 'placeholder': 'E-mail'}),
        error_messages={"required": "*Required Field"}
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'id': 'password', 'class': 'registration__password', 'type': 'password', 'name': 'password',
                   'placeholder': 'Password'}),
        min_length=8,
        error_messages={"required": "*Required Field", "max_length": "Min password length is 8 Characters"}
    )

    class Meta:
        model = AuthUser
        fields = ('email', 'password')


class RegisterForm(BaseForm):
    field_order = ['name', 'surname']
    password_confirm = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'id': 'repeat_password', 'class': 'registration__password', 'type': 'password', 'name': 'repeat_password',
                   'placeholder': 'Password'}),
        min_length=8,
        error_messages={"required": "*Required Field", "max_length": "Min password length is 8 Characters"}
    )
    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'id': 'name', 'class': 'registration__password', 'type': 'text', 'name': 'name',
                   'placeholder': 'Your name'}),
        min_length=2,
        error_messages={"required": "*Required Field", "max_length": "Name can't be less 2 Characters"}
    )
    surname = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'id': 'sur_name', 'class': 'registration__password', 'type': 'text', 'name': 'sur_name',
                   'placeholder': 'Your Surname'}),
        min_length=2,
        error_messages={"required": "*Required Field", "max_length": "Surame can't be less 2 Characters"}
    )

    class Meta:
        model = User
        fields = "__all__"


