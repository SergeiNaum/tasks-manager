from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from tasks import models
from users.models import User


class TaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = ["name", "description", "status", "executor", "labels"]
