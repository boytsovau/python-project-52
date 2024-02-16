from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.contrib.messages import get_messages
from task_manager.mark.models import Mark
from tests import FIXTURE_DIR


class DeleteMark(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_mark.json"]

    def test_delete_open_without_login(self):
        response = self.client.get(reverse('mark_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Вы не авторизованы! Пожалуйста, выполните вход.',
                      [msg.message for msg in messages])

    def test_delete_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('mark_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('mark_delete', kwargs={'pk': 1})
        )
        statuses = Mark.objects.all()
        self.assertEqual(len(statuses), 0)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Метка успешно удалена',
                      [msg.message for msg in messages])
