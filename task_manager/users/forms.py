from django import forms
from django.utils.translation import gettext_lazy as _
from .models import TaskUser as User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=_('Your password must contain '
                    'at least 8 characters.'),
    )

    password2 = forms.CharField(
        label=_('Password confirmation'),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=_('Enter the same password as before, '
                    'for verification.'),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'password1', 'password2']

        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'username': _('Username'),
        }

        help_texts = {
            'username': _('Required. 150 characters or fewer. '
                          'Letters, digits and @/./+/-/_ only.'),

            'password2': _('Enter the same password as before, '
                           'for verification.')
        }
