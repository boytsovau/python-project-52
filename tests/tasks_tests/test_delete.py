from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from django.utils.translation import gettext as _
from task_manager.task.models import Task
from tests import FIXTURE_DIR


class DeleteTask(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db_task.json"]

    def test_delete_task_open_without_login(self):
        response = self.client.get(reverse('task_delete', kwargs={'pk': 1}),
                                   follow=True)
        self.assertEqual(response.status_code, 200)

        expected_message = _('Please login')
        self.assertContains(response, expected_message)

    def test_delete_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('task_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('task_delete', kwargs={'pk': 1}), follow=True
        )
        self.assertEqual(Task.objects.all().count(), 0)

        expected_message = _('Task was successfully deleted')
        self.assertContains(response, expected_message)
