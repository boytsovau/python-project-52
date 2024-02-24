from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Mark


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['name']
        labels = {
            'name': _('Name'),
        }
