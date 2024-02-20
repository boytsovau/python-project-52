from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.users.models import TaskUser as User
from django.contrib.messages import get_messages
from tests import load_fixture_data


class CreateTest(TestCase):

    def test_open_create_page(self):
        response = self.client.get(reverse('user_add'))
        self.assertEqual(response.status_code, 200)

    def test_create_redirect_user(self):
        testuser = load_fixture_data('user.json')
        response = self.client.post(
            reverse('user_add'),
            testuser
        )
        self.assertRedirects(response, reverse('user_login'))
        user = User.objects.get(username=testuser.get('username'))
        self.assertEqual(user.username, testuser.get('username'))

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Пользователь успешно зарегистрирован',
                      [msg.message for msg in messages])
