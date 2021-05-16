from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from onlinepizzas.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime


def only_int(value):
    if not value.isdigit():
        raise ValidationError('Введите верный номер')
    if len(value) != 11:
        raise ValidationError('Введите 11 цифр, начиная с 8')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    number = forms.CharField(required=True, validators=[only_int])
    birthday = forms.DateField(required=True, widget=forms.SelectDateWidget(
        years=range(int(datetime.datetime.now().year - 90), int(datetime.datetime.now().year + 1))))

    class Meta:
        model = User
        fields = (
            'number',
            'first_name',
            'last_name',
            'middle_name',
            'birthday',
            'email',
            'password1',
            'password2'
        )
        labels = {
            'number': 'Номер',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'birthday': 'Дата рождения',
            'email': 'E-Mail',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль'
        }
        widgets = {
            'birthday': forms.DateField
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return User
