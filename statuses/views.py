from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

from statuses.forms import StatusForm
from statuses.models import Status
from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin


# Create your views here.
class StatusesListView(AuthRequiredMixin, ListView):
    template_name = 'statuses/statuses.html'
    model = Status
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _('Task Manager')
        context['title'] = _('Task Manager')
        context['current_page'] = 'statuses'
        return context


class StatusCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):

    template_name = 'statuses/statuses_form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _('Task Manager')
        context['title'] = _('Task Manager')
        context['button_text'] = _('Create')
        context['current_page'] = 'statuses'
        return context


class StatusUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):

    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully changed')
    extra_context = {
        'title': _('Change status'),
        'button_text': _('Change'),
    }


class StatusDeleteView(AuthRequiredMixin, DeleteProtectionMixin,
                       SuccessMessageMixin, DeleteView):

    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')
    protected_message = _('It is not possible to delete a status '
                          'because it is in use')
    protected_url = reverse_lazy('statuses')
    extra_context = {
        'title': _('Delete status'),
        'button_text': _('Yes, delete'),
    }