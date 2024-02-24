from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class UserTestCustomMixin(UserPassesTestMixin):
    modify_error_message = ''
    success_url = ''

    def test_func(self):
        user_instance = self.request.user
        obj = self.get_object()
        if user_instance.id == obj.id:
            return True
        return False

    def handle_no_permission(self):
        messages.error(self.request, self.modify_error_message)
        return redirect(self.success_url)
