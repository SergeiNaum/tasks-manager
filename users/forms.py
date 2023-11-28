from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext as _
from django import forms

from users.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label=_('username'), widget=forms.TextInput(
        attrs={'class': 'form-input form-control', 'placeholder': _('username')}))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-input form-control', 'placeholder': _('Password')}))

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label=_('username'), widget=forms.TextInput(
        attrs={
            'class': 'form-input form-control', 'placeholder': _('username')
        }))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={
            'class': 'form-input form-control', 'placeholder': _('Password')
        }))
    password2 = forms.CharField(label=_('Password2'), widget=forms.PasswordInput(
        attrs={
            'class': 'form-input form-control', 'placeholder': _('Password2')
        }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-input form-control', 'placeholder': _('First name')}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-input form-control', 'placeholder': _('Last name')}
            ),
        }


class UserEditForm(forms.ModelForm):

    username = forms.CharField(label=_('username'), widget=forms.TextInput(
        attrs={
            'class': 'form-input form-control', 'placeholder': _('username')
        }))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={
            'class': 'form-input form-control', 'placeholder': _('Password')
        }))
    password2 = forms.CharField(label=_('Password2'), widget=forms.PasswordInput(
        attrs={
            'class': 'form-input form-control', 'placeholder': _('Password2')
        }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-input form-control', 'placeholder': _('First name')}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-input form-control', 'placeholder':  _('Last name')}
            ),
        }


