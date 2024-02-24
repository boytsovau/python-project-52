from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.utils.translation import gettext as _
from task_manager.task.models import Status, Task
from tests import FIXTURE_DIR, load_fixture_data


class Create(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_task.json"]

    def setUp(self):
        self.TEST_TASK = load_fixture_data('data.json')
        self.task_name = self.TEST_TASK.get('task').get('name')

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
        initial_task_count = Task.objects.all().count()
        response = self.client.post(
            reverse('task_add'),
            {'name': self.task_name,
             'author': user.id,
             'status': status.id
             },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.all().count(), initial_task_count + 1)

        expected_message = _('Task created successfully')
        self.assertContains(response, expected_message)
