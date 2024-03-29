import django_filters
from django import forms
from .models import Task
from task_manager.status.models import Status
from task_manager.users.models import TaskUser as User
from django.utils.translation import gettext_lazy as _
from task_manager.mark.models import Mark


class MarkFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        label=_('Status'),
        queryset=lambda req: Status.objects.all(),
    )
    executor = django_filters.ModelChoiceFilter(
        label=_('Executor'),
        queryset=lambda req: User.objects.all(),
    )
    labels = django_filters.ModelChoiceFilter(
        label=_('Label'),
        queryset=lambda req: Mark.objects.all(),
    )
    self_tasks = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        label=_('Only self tasks'),
        method='get_self_tasks'
    )

    def get_self_tasks(self, queryset, field_name, value):
        result = queryset.filter(author_id=self.request.user.id)
        return result if value else queryset

    class Meta:
        model = Task
        fields = []
