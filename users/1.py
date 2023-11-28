











class UserCreateView(SuccessMessageMixin, CreateView):
    """
    Create new user.
    """
    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')
    extra_context = {
        'title': _('Create user'),
        'button_text': _('Register'),
    }


class UserUpdateView(AuthRequiredMixin, UserPermissionMixin,
                     SuccessMessageMixin, UpdateView):
    """
    Edit existing user.

    Authorization required.
    The user can only edit himself.
    """
    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users')
    extra_context = {
        'title': _('Update user'),
        'button_text': _('Update'),
    }


class UserDeleteView(AuthRequiredMixin, UserPermissionMixin,
                     DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    """
    Delete existing user.

    Authorization required.
    The user can only delete himself.
    If a user is associated with tasks, he cannot be deleted.
    """
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User is successfully deleted')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users')
    protected_message = _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('users')
    extra_context = {
        'title': _('Delete user'),
        'button_text': _('Yes, delete'),
    }