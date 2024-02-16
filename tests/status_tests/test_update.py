from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.contrib.messages import get_messages
from task_manager.status.models import Status
from tests import FIXTURE_DIR


class UpdateStatus(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_status.json"]

    def test_update_open_without_login(self):
        response = self.client.get(reverse('status_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Вы не авторизованы! Пожалуйста, выполните вход.',
                      [msg.message for msg in messages])

    def test_update_task(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('status_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('status_update', kwargs={'pk': 1}),
            {'name': 'test'}
        )
        status = Status.objects.get(pk=1)
        self.assertEqual(status.name, 'test')
