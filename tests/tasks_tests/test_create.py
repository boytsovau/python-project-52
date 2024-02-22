from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.utils.translation import gettext as _
from task_manager.task.models import Status, Task
from tests import FIXTURE_DIR


class Create(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_task.json"]

    def test_create_open_without_login(self):
        response = self.client.get(reverse('task_add'), follow=True)
        self.assertEqual(response.status_code, 200)

        expected_message = _('Please login')
        self.assertContains(response, expected_message)

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
             },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.all().count(), 2)

        expected_message = _('Task created successfully')
        self.assertContains(response, expected_message)
