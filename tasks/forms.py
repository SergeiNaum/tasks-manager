from django import forms
from django.utils.translation import gettext_lazy as _

from tasks import models
from users.models import User


class TaskForm(forms.ModelForm):

    def clean_executor(self):
        user_id = self.cleaned_data["executor"]
        user = User.objects.get(id=user_id)
        return user

    executor = forms.ChoiceField(
        choices=[("", "---------")] + [(e.id, e.fullname) for e in User.objects.all()],
        label=_("Executor"))

    class Meta:
        model = models.Task
        fields = ["name", "description", "status", "executor", "labels"]
