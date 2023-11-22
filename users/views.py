from django.urls import reverse_lazy
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import ListView, FormView, TemplateView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import DeleteView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from users.forms import LoginUserForm, RegisterUserForm, UserEditForm
from users.models import User


# Create your views here.
class UsersIndexView(TemplateView):
    template_name = 'users/all_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['logo'] = _('Task Manager')
        context['title'] = _('Task Manager')
        context['current_page'] = 'users_index'
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': _('Task Manager'),
                     'logo': _('Task Manager'),
                     'current_page': 'login'
                     }


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': _('Task Manager'),
                     'logo': _('Task Manager'),
                     'current_page': 'register'
                     }
    success_url = reverse_lazy('users:register_done')


class RegisterDone(TemplateView):
    template_name = 'users/register_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _('Task Manager')
        context['title'] = _('Task Manager')
        context['current_page'] = 'register'
        return context


class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'users/update_user_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _('Task Manager')
        context['title'] = _('Task Manager')
        context['current_page'] = 'users_index'
        return context
    def get_object(self):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = User.objects.get(id=self.kwargs['pk'])
        return kwargs

    def get_success_url(self):
        return reverse('users:users_index')

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class UserDeleteView(DeleteView):
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('users:users_index')
    template_name = 'users/delete_user.html'

    def get_object(self, queryset=None):
        return self.get_queryset().get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _('Task Manager')
        context['title'] = _('Task Manager')
        context['current_page'] = 'users_index'
        # context['fullname'] = f'{User.first_name} {User.last_name}'
        return context

