from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.contrib.messages import get_messages
from task_manager.mark.models import Mark
from tests import FIXTURE_DIR


class UpdateStatus(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_mark.json"]

    def test_update_open_without_login(self):
        response = self.client.get(reverse('mark_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Вы не авторизованы! Пожалуйста, выполните вход.',
                      [msg.message for msg in messages])

    def test_update_mark(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('mark_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('mark_update', kwargs={'pk': 1}),
            {'name': 'test'}
        )
        mark = Mark.objects.get(pk=1)
        self.assertEqual(mark.name, 'test')

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Метка успешно изменена',
                      [msg.message for msg in messages])
