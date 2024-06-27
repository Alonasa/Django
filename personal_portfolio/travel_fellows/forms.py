from django import forms


class AuthorizeForm(forms.Form):
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'id': 'email', 'class': 'registration__email', 'name': 'email', 'placeholder': 'E-mail'}))
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'registration__password', 'type': 'password', 'name': 'password',
                                          'placeholder': 'Password'}))