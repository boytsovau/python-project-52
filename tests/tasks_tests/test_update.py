from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from django.utils.translation import gettext as _
from task_manager.task.models import Status, Task
from tests import FIXTURE_DIR, load_fixture_data


class UpdateTask(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db_task.json"]

    def setUp(self):
        self.TEST_USER = load_fixture_data('user.json')
        self.username = self.TEST_USER.get('username')
        self.password = self.TEST_USER.get('password')

    def test_update_open_without_login(self):
        response = self.client.get(reverse('task_update', kwargs={'pk': 1}),
                                   follow=True)
        self.assertEqual(response.status_code, 200)

        expected_message = _('Please login')
        self.assertContains(response, expected_message)

    def test_update_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('task_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        task = Task.objects.all().first()
        status = Status.objects.all().first()
        user2 = User.objects.create_user(username=self.username,
                                         password=self.password)
        task2 = {
            'name': 'test_task',
            'status': status.id,
            'executor': user2.id,
        }
        response = self.client.post(
            reverse('task_update', kwargs={'pk': task.id}),
            task2,
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        task = Task.objects.get(pk=task.id)
        self.assertEqual(task.name, task2['name'])
        self.assertEqual(task.executor_id, task2['executor'])

        expected_message = _('Task updated successfully')
        self.assertContains(response, expected_message)
