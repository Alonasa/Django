from datetime import datetime, timedelta

from django import forms
from django.core.validators import FileExtensionValidator
from django.forms import ModelForm, Form
from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django_flatpickr.schemas import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput

from .models import User, UserTransportation, UserPlans


class BaseForm(ModelForm):
    username = forms.EmailField(
        label='',
        widget=forms.TextInput(
            attrs={'id': 'username', 'class': 'registration__email', 'name': 'username', 'placeholder': 'E-mail'}),
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


class AuthorizeForm(Form):
    username = forms.EmailField(
        label='',
        widget=forms.TextInput(
            attrs={'id': 'username', 'class': 'registration__email', 'name': 'username', 'placeholder': 'E-mail'}),
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


class RegisterForm(BaseForm):
    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'username',
            'password',
            'password_confirm',
        ]

    field_order = [
        'name',
        'surname',
    ]
    password_confirm = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'id': 'repeat_password',
                'class': 'registration__password',
                'type': 'password',
                'name': 'repeat_password',
                'placeholder': 'Password',
            }
        ),
        min_length=8,
        error_messages={
            "required": "*Required Field",
            "max_length": "Min password length is 8 Characters",
        }
    )
    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'id': 'name',
                'class': 'registration__password',
                'type': 'text',
                'name': 'name',
                'placeholder': 'Your name',
            }
        ),
        min_length=2,
        error_messages={
            "required": "*Required Field",
            "max_length": "Name can't be less 2 Characters",
        }
    )
    surname = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'id': 'sur_name',
                'class': 'registration__password',
                'type': 'text',
                'name': 'sur_name',
                'placeholder': 'Your Surname',
            }
        ),
        min_length=2,
        error_messages={
            "required": "*Required Field",
            "max_length": "Surname can't be less 2 Characters",
        }
    )


class UserPhotoForm(Form):
    user_photo = forms.ImageField(
        label='Change photo',
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'visually-hidden',
                'id': 'upload-photo',
                'onchange': 'this.form.submit()',
            }
        ),
        validators=[
            FileExtensionValidator(allowed_extensions=[
                'jpg',
                'jpeg',
                'png',
            ])
        ]
    )


class UserHashtagsForm(Form):
    hashtags = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'user-information__textfield',
                'rows': '1',
                'placeholder': 'Short information about your interests in 6-10 tags',
                'onchange': 'this.form.submit()',
            }
        )
    )


class UserTransportationForm(ModelForm):
    class Meta:
        model = UserTransportation
        fields = [
            'plane',
            'bus',
            'bike',
            'feet',
        ]

    def render_field(self, name):
        label_class = 'transport-type user-information__transport-type'
        icon_class = f'transport-type__icon transport-type__icon--{name if name != "feet" else "run"}'
        icon_svg = format_html(
            f'<svg class="{icon_class}" width="13" height="16">'
            f'<use xlink:href="{static("img/travel_fellows/sprite.svg")}#icon-{name if name != "feet" else "run"}">'
            f'</use>'
            f'</svg>',
            icon_class, static("img/travel_fellows/sprite.svg"), name
        )
        label = f'<label class="{label_class}" for="{name}">{icon_svg}</label>'
        input = (f'<input class="visually-hidden" type="checkbox" name="{name}" id="{name}" onchange=this.form.submit()'
                 f' {"checked" if getattr(self.instance, name, True) else ""}>')

        return format_html(
            f'<li class="user-information__transport-item" '
            f'data-tooltip="{name.capitalize()}">{input}{label}</li>',
            name.capitalize(), input, label
        )

    def as_p(self):
        return mark_safe(''.join(f'{self.render_field(name)}' for name in self.fields))

class CalendarWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        if value:
            current_date = value
        else:
            current_date = datetime.now()

        # Get the first day of the current month
        first_day_of_month = datetime(current_date.year, current_date.month, 1)

        # Get the last day of the current month
        last_day_of_month = (first_day_of_month + timedelta(days=32)).replace(day=1) - timedelta(
            days=1)

        # Determine the starting day of the week (Monday)
        start_day = first_day_of_month.weekday()

        # Generate the calendar HTML
        calendar_html = f'<table class="calendar">'
        calendar_html += '<thead><tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr></thead>'
        calendar_html += '<tbody><tr>'

        # Fill in the dates for the previous month's days
        for i in range(start_day):
            calendar_html += f'<td class="prev-month">{first_day_of_month - timedelta(days=start_day - i)}</td>'

        # Fill in the dates for the current month
        current_day = first_day_of_month
        while current_day <= last_day_of_month:
            if current_day.weekday() == 0 and current_day != first_day_of_month:
                calendar_html += '</tr><tr>'
            calendar_html += f'<td>{current_day.day}</td>'
            current_day += timedelta(days=1)

        # Fill in the dates for the next month's days
        while len(calendar_html.split('<td>')) - 1 < 42:
            calendar_html += f'<td class="next-month">{current_day.day}</td>'
            current_day += timedelta(days=1)

        calendar_html += '</tr></tbody></table>'
        return calendar_html



class UserPlansForm(ModelForm):
    class Meta:
        model = UserPlans
        fields = '__all__'

    companions = forms.IntegerField(
        label='',
        widget=forms.NumberInput(
            attrs={
                'class': 'plan-step__number-input',
                'id': 'teammates-quantity',
                'name': 'teammates-quantity',
                'min': '1',
                'value': '2',
            }
        ),
    )
    length = forms.IntegerField(
        label='',
        widget=forms.NumberInput(
            attrs={
                'class': 'plan-step__number-input',
                'id': 'travel-term',
                'name': 'travel-term',
                'min': '1',
                'value': '2',
            },
        )
    )

    kids = forms.BooleanField(
        label=mark_safe('<label class="plan-step__custom-checkbox" for="with-kids">With kids?</label>'),
        widget=forms.CheckboxInput(
            attrs={
                'class': 'visually-hidden',
                'name': 'with-kids',
                'id': 'with-kids',
            }
        )
    )

    cale = forms.DateField(widget=DatePickerInput({'mode': 'range'}, options=FlatpickrOptions(static='true', inline='true', appendTo='calendar__title', showAlways="true")))
