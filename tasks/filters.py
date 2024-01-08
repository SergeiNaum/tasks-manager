from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django import forms
from django.utils.translation import gettext_lazy as _

from labels.models import Label
from tasks.models import Task


class TaskFilterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        self.fields['executor'].label_from_instance = lambda obj: obj.fullname

    class Meta:
        model = Task
        fields = ["status", "executor"]


class TaskFilter(FilterSet):
    labels = ModelChoiceFilter(queryset=Label.objects.all(), label=_("Label"))

    own_tasks = BooleanFilter(
        label=_("Only own tasks"),
        widget=forms.CheckboxInput,
        method="get_own_tasks",
    )

    def get_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        form = TaskFilterForm
        model = Task
        fields = ["status", "executor"]
