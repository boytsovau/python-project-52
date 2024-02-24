from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import DeletionMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginRequiredCustomMixin(LoginRequiredMixin):
    permission_denied_message = _('Please login to modify user')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.permission_denied_message)
            return redirect(reverse_lazy('user_login'))

        return super().dispatch(request, *args, **kwargs)


class DeleteProtectErrorMixin(DeletionMixin):
    protected_error_message = ''
    success_message = ''

    def form_valid(self, form):
        try:
            super().delete(self.request)
        except ProtectedError:
            messages.error(self.request, self.protected_error_message)
        else:
            messages.info(self.request, self.success_message)
        return redirect(self.get_success_url())


class PermissionDeniedMessageMixin(LoginRequiredMixin):
    permission_denied_message = _('Please login to delete user')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.permission_denied_message)
            return redirect(reverse_lazy('user_login'))

        return super().dispatch(request, *args, **kwargs)
