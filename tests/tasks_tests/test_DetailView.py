from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from django.contrib.messages import get_messages
from task_manager.task.models import Task
from tests import FIXTURE_DIR


class List(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db_task.json"]

    def test_list_without_login(self):
        response = self.client.get(reverse(
            'task_view', args=[1]))
        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Вы не авторизованы! Пожалуйста, выполните вход.',
                      [msg.message for msg in messages])

    def test_list_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        self.assertEqual(Task.objects.all().count(), 1)
        task = Task.objects.all().first()
        response = self.client.get(reverse(
            'task_view', args=[task.id]))
        self.assertEqual(response.status_code, 200)
