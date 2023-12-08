from django.urls import reverse_lazy
from django.views.generic import (CreateView,
                                  UpdateView,
                                  DeleteView,
                                  ListView)
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

from labels.forms import LabelForm
from labels.models import Label
from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin


class LabelsListView(AuthRequiredMixin, ListView):
    """
    Show all labels.

    Authorisation required.
    """
    template_name = 'labels/labels.html'
    model = Label
    context_object_name = 'labels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _('Task Manager')
        context['title'] = _('Task Manager')
        context['current_page'] = 'labels'
        return context


class LabelCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Create new label.

    Authorisation required.
    """
    template_name = 'labels/labels_form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:all_labels')
    success_message = _('Label successfully created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _('Task Manager')
        context['title'] = _('Task Manager')
        context['button_text'] = _('Create')
        context['current_page'] = 'labels'
        return context


class LabelEditView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit existing label.

    Authorisation required.
    """
    template_name = 'labels/labels_form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:all_labels')
    success_message = _('Label successfully changed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _('Task Manager')
        context['title'] = _('Task Manager')
        context['button_text'] = _('Change label')
        context['current_page'] = 'labels'
        return context


class LabelDeleteView(AuthRequiredMixin, DeleteProtectionMixin,
                      SuccessMessageMixin, DeleteView):
    """
    Delete existing label.

    Authorization required.
    If the label is associated with at least one task it cannot be deleted.
    """
    template_name = 'labels/delete.html'
    model = Label
    success_url = reverse_lazy('labels:all_labels')
    success_message = _('Label successfully deleted')
    protected_message = _('It is not possible to delete a label '
                          'because it is in use')
    protected_url = reverse_lazy('labels:all_labels')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _('Task Manager')
        context['title'] = _('Task Manager')
        context['button_text'] = _('Yes, delete')
        context['current_page'] = 'labels'
        return context
