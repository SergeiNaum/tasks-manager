from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from manager.forms import LoginUserForm


# Create your views here.
class IndexView(TemplateView):
    template_name = "manager/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logo"] = _("Task Manager")
        context["title"] = _("Task Manager")
        context["current_page"] = "index"
        context["user"] = self.request.user
        return context


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = "manager/login.html"
    next_page = reverse_lazy("index")
    success_message = _("You are logged in")
    extra_context = {
        "title": _("Task Manager"),
        "logo": _("Task Manager"),
        "button_text": _("Enter"),
        "current_page": "login",
    }


class LogoutUser(LogoutView):
    next_page = reverse_lazy("index")
    success_message = _("You are logged out")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)
