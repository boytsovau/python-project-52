from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from task_manager.mixins import DeleteProtectErrorMixin, \
    LoginRequiredCustomMixin
from task_manager.status.forms import StatusForm
from task_manager.status.models import Status
from django.utils.translation import gettext_lazy as _


class StatusListView(LoginRequiredCustomMixin, ListView):
    model = Status
    template_name = "status/list.html"
    extra_context = {
        'statuses': _('Statuses'),
        'ID': _('ID'),
        'name': _('Name'),
        'created_at': _('Created at'),
    }
    permission_denied_message = _('Please login')


class StatusCreateView(LoginRequiredCustomMixin, SuccessMessageMixin,
                       CreateView):
    form_class = StatusForm
    template_name = "status/create.html"
    success_url = reverse_lazy('status_list')
    extra_context = {
        'header': _('Create status'),
        'button_title': _('Create'),
    }
    success_message = _('Status created successfully')
    permission_denied_message = _('Please login')


class StatusUpdateView(LoginRequiredCustomMixin, SuccessMessageMixin,
                       UpdateView):
    model = Status
    form_class = StatusForm
    template_name = "status/create.html"
    success_url = reverse_lazy('status_list')
    extra_context = {
        'header': _('Update status'),
        'button_title': _('Update'),
    }
    success_message = _('Status updated successfully')
    permission_denied_message = _('Please login')


class StatusDeleteView(LoginRequiredCustomMixin, DeleteProtectErrorMixin,
                       DeleteView):
    model = Status
    template_name = "delete.html"
    success_url = reverse_lazy('status_list')
    extra_context = {
        'header': _('Remove status'),
        'button_title': _('Yes, remove'),
        'message': _('Are you sure delete'),
    }
    permission_denied_message = _('Please login')
    protected_error_message = _('Status can\'t be deleted - on use now')
    success_message = _('Status was deleted successfully')
