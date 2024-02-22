from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from django.utils.translation import gettext as _
from task_manager.task.models import Task
from tests import FIXTURE_DIR


class List(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db_task.json"]

    def test_list_without_login(self):
        response = self.client.get(reverse(
            'task_view', args=[1]),
            follow=True)
        self.assertEqual(response.status_code, 200)

        expected_message = _('Please login')
        self.assertContains(response, expected_message)

    def test_list_with_login(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        self.assertEqual(Task.objects.all().count(), 1)
        task = Task.objects.all().first()
        response = self.client.get(reverse(
            'task_view', args=[task.id]))
        self.assertEqual(response.status_code, 200)
