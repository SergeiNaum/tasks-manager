from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView

from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin
from users.models import User
from tasks.models import Task
from tasks.forms import TaskForm
from tasks.filters import TaskFilter


class TasksListView(AuthRequiredMixin, FilterView):
    """
    Show all tasks.

    Authorisation required.
    """

    template_name = "tasks/tasks.html"
    model = Task
    filterset_class = TaskFilter
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logo"] = _("Task Manager")
        context["title"] = _("Task Manager")
        context["button_text"] = _("Show")
        context["current_page"] = "tasks"
        context["user"] = self.request.user
        return context


class TaskDetailView(AuthRequiredMixin, DetailView):
    """
    Show one task details.

    Authorisation required.
    """

    template_name = "tasks/task_detail.html"
    model = Task
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logo"] = _("Task Manager")
        context["title"] = _("Task Manager")
        context["current_page"] = "tasks"
        return context


class TaskCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Create new task.

    Authorisation required.
    """

    template_name = "tasks/tasks_form.html"
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:tasks")
    success_message = _("Task successfully created")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logo"] = _("Task Manager")
        context["title"] = _("Task Manager")
        context["button_text"] = _("Create")
        context["current_page"] = "tasks"
        return context

    def form_valid(self, form):
        """
        Set current user as the task's author.
        """
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskEditView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit existing task.

    Authorisation required.
    """

    template_name = "tasks/tasks_form.html"
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:tasks")
    success_message = _("Task successfully changed")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logo"] = _("Task Manager")
        context["title"] = _("Task Manager")
        context["button_text"] = _("Change")
        context["current_page"] = "tasks"
        return context


class TaskDeleteView(
    AuthRequiredMixin, AuthorDeletionMixin, SuccessMessageMixin, DeleteView
):
    """
    Delete existing task.

    Authorization required.
    Only the author can delete his tasks.
    """

    template_name = "tasks/delete.html"
    model = Task
    success_url = reverse_lazy("tasks:tasks")
    success_message = _("Task successfully deleted")
    author_message = _("The task can be deleted only by its author")
    author_url = reverse_lazy("tasks:tasks")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logo"] = _("Task Manager")
        context["title"] = _("Task Manager")
        context["button_text"] = _("Yes, delete")
        context["current_page"] = "tasks"
        return context
