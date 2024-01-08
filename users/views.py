from django.urls import reverse_lazy
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView
from django.contrib.auth import update_session_auth_hash

from task_manager.mixins import (
    UserPermissionMixin,
    AuthRequiredMixin,
    DeleteProtectionMixin,
)
from users.forms import RegisterUserForm, UserEditForm
from users.models import User


# Create your views here.
class UsersIndexView(TemplateView):
    template_name = "users/all_users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        context["logo"] = _("Task Manager")
        context["title"] = _("Task Manager")
        context["current_page"] = "users_index"
        return context


class RegisterUser(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_message = _("User is successfully registered")
    # success_url = reverse_lazy("users:register_done")
    success_url = reverse_lazy("login")
    extra_context = {
        "title": _("Task Manager"),
        "logo": _("Task Manager"),
        "button_text": _("Register"),
        "current_page": "register",
    }


class RegisterDone(TemplateView):
    template_name = "users/register_done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logo"] = _("Task Manager")
        context["title"] = _("Task Manager")
        context["current_page"] = "register"
        return context  # noqa E501


class UserEditView(
    AuthRequiredMixin, UserPermissionMixin, SuccessMessageMixin, UpdateView
):
    model = User
    form_class = UserEditForm
    template_name = "users/edit_user_form.html"
    success_message = _("User is successfully updated")
    permission_message = _("You have no rights to change another user.")
    permission_url = reverse_lazy("users:users_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logo"] = _("Task Manager")
        context["title"] = _("Task Manager")
        context["button_text"] = _("Edit")
        context["current_page"] = "users_index"
        return context

    def get_object(self):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = User.objects.get(id=self.kwargs["pk"])
        return kwargs

    def get_success_url(self):
        return reverse("users:users_index")

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)  # noqa E501
        return super().form_valid(form)


class UserDeleteView(
    AuthRequiredMixin,
    UserPermissionMixin,
    DeleteProtectionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    context_object_name = "user"
    template_name = "users/delete_user.html"
    success_url = reverse_lazy("users:users_index")
    success_message = _("User is successfully deleted")
    permission_message = _("You have no rights to change another user.")
    permission_url = reverse_lazy("users:users_index")
    protected_message = _("Unable to delete a user because he is being used")
    protected_url = reverse_lazy("users:users_index")

    def get_object(self, queryset=None):
        return self.get_queryset().get(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logo"] = _("Task Manager")
        context["title"] = _("Task Manager")
        context["button_text"] = _("Yes, delete")
        context["current_page"] = "users_index"
        return context
