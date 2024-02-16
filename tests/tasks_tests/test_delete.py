from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from django.contrib.messages import get_messages
from task_manager.task.models import Task
from tests import FIXTURE_DIR


class DeleteTask(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db_task.json"]

    def test_delete_task_open_without_login(self):
        response = self.client.get(reverse('task_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Вы не авторизованы! Пожалуйста, выполните вход.',
                      [msg.message for msg in messages])

    def test_delete_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('task_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('task_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.all().count(), 0)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Задача успешно удалена',
                      [msg.message for msg in messages])
