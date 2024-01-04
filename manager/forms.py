from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _
from users import models


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label=_("username"),
        widget=forms.TextInput(
            attrs={"class": "form-input form-control", "placeholder": _("username")}
        ),
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={"class": "form-input form-control", "placeholder": _("Password")}
        ),
    )

    class Meta:
        model = models.User
        fields = ["username", "password"]

