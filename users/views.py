from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, FormView, TemplateView, DetailView, CreateView
from django.contrib.auth.views import LoginView

from users.forms import LoginUserForm, RegisterUserForm
from users.models import User


# Create your views here.
class UsersIndexView(TemplateView):
    template_name = 'users/all_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['logo'] = _("Task Manager")
        context['title'] = _("Task Manager")
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': _("Task Manager"),
                     'logo': _("Task Manager")
                     }


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': _("Task Manager"),
                     'logo': _("Task Manager")
                     }
    success_url = reverse_lazy('users:register_done')


class RegisterDone(TemplateView):
    template_name = 'users/register_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _("Task Manager")
        context['title'] = _("Task Manager")
        return context
