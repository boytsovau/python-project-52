from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {
        'header': _('Task manager'),
    }


class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('root')
    extra_context = {
        'header': _('Enter'),
        'button_title': _('Entrance'),
    }

    def form_valid(self, form):
        messages.info(self.request, _('Login successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Login Error'))
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('root')
    message = _('You have successfully logged out')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, message=self.message)
        return super().dispatch(request, *args, **kwargs)
