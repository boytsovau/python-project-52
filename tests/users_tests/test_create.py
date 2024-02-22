from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.users.models import TaskUser as User
from django.utils.translation import gettext as _
from tests import load_fixture_data


class CreateTest(TestCase):

    def test_open_create_page(self):
        response = self.client.get(reverse('user_add'))
        self.assertEqual(response.status_code, 200)

    def test_create_redirect_user(self):
        testuser = load_fixture_data('user.json')
        response = self.client.post(
            reverse('user_add'),
            testuser,
            follow=True
        )
        self.assertRedirects(response, reverse('user_login'))
        user = User.objects.get(username=testuser.get('username'))
        self.assertEqual(user.username, testuser.get('username'))

        expected_message = _('User created successfully')
        self.assertContains(response, expected_message)
