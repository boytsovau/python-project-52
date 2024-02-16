from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.contrib.messages import get_messages
from task_manager.status.models import Status
from tests import FIXTURE_DIR


class Create(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_status.json"]

    def test_create_open_without_login(self):
        response = self.client.get(reverse('status_add'))
        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Вы не авторизованы! Пожалуйста, выполните вход.',
                      [msg.message for msg in messages])

    def test_create_task(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        statuses = Status.objects.all()
        response = self.client.get(reverse('status_add'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(statuses), 1)
        response = self.client.post(
            reverse('status_add'),
            {'name': 'test'}
        )
        statuses2 = Status.objects.all()
        self.assertEqual(len(statuses2), 2)
        status_added = statuses2[1]
        self.assertEqual(status_added.name, 'test')

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Статус успешно создан',
                      [msg.message for msg in messages])
