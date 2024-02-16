from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.contrib.messages import get_messages
from task_manager.task.models import Status, Task
from tests import FIXTURE_DIR


class Create(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_task.json"]

    def test_create_open_without_login(self):
        response = self.client.get(reverse('task_add'))
        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Вы не авторизованы! Пожалуйста, выполните вход.',
                      [msg.message for msg in messages])

    def test_create_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        status = Status.objects.all().first()
        response = self.client.get(reverse('task_add'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.all().count(), 1)
        response = self.client.post(
            reverse('task_add'),
            {'name': 'test task',
             'author': user.id,
             'status': status.id
             }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.all().count(), 2)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Задача успешно создана',
                      [msg.message for msg in messages])
