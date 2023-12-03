from django import forms
from django.utils.translation import gettext as _

from tasks import models


class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['name', 'description', 'status', 'executor', 'labels']

