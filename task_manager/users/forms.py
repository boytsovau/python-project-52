from django.utils.translation import gettext_lazy as _
from .models import TaskUser as User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username']

        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'username': _('Username'),
        }

        help_texts = {
            'username': _('Required. 150 characters or fewer. '
                          'Letters, digits and @/./+/-/_ only.')
        }
