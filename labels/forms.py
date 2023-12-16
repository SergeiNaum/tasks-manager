from django import forms
from django.utils.translation import gettext as _

from labels import models


class LabelForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name"),
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-input form-control", "placeholder": _("Name")}
        ),
    )

    class Meta:
        model = models.Label
        fields = ("name",)
