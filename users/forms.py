from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input form-control', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={
            'class': 'form-input form-control', 'placeholder': 'Имя пользователя'
        }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'class': 'form-input form-control', 'placeholder': 'Пароль'
        }))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={
            'class': 'form-input form-control', 'placeholder': 'Подтверждение пароля'
        }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-input form-control', 'placeholder': 'Имя'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-input form-control', 'placeholder': 'Фамилия'}
            ),
        }