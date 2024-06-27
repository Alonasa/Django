from django import forms


class AuthorizeForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'id': 'email', 'class': 'registration__email', 'name': 'email', 'placeholder': 'E-mail'}))
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'registration__password', 'type': 'password', 'name': 'password',
                                          'placeholder': 'Password'}))
    # submit_button = forms(
    #     label='',
    #     required=False,
    #     widget=forms.Submit(
    #         attrs={
    #             'class': 'button button--registration registration__submit',
    #             'type': 'submit',
    #             'value': '{% if login %} Login {% else %} Register {% endif %}'
    #         }
    #     )
    # )
