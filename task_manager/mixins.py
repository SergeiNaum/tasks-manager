from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.urls import reverse
from django.http import HttpResponseRedirect


class AuthRequiredMixin(LoginRequiredMixin):
    """
    Authentication check.
    Restricts access without authentication.
    """
    auth_message = _('You are not logged in! Please log in.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_message)
            return redirect(reverse_lazy('users:login'))

        return super().dispatch(request, *args, **kwargs)


class UserPermissionMixin(UserPassesTestMixin):
    """
    Authorisation check.
    Prohibits changing an item created by another user.
    """
    permission_message = None
    permission_url = None

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(self.permission_url)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('change_user_data'):
            # Check if the user has permission to change user data
            if int(kwargs['pk']) != request.user.id:
                # If the user is attempting to change another user's data
                messages.error(request, self.permission_message)
                return HttpResponseRedirect(reverse('users:users_index'))
        return super().dispatch(request, *args, **kwargs)


class DeleteProtectionMixin:
    """
    Association check.
    Prohibits deleting an object if it is used by other objects.
    """
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)


class AuthorDeletionMixin(UserPassesTestMixin):
    """
    Authorisation check.
    Prohibits deleting an item not by its author.
    """
    author_message = None
    author_url = None

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.author_message)
        return redirect(self.author_url)
