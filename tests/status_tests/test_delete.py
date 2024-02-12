from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.status.models import Status
import os

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../fixtures'
)


class Deletestatus(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_status.json"]

    def test_delete_open_without_login(self):
        response = self.client.get(reverse('status_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_delete_task(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('status_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('status_delete', kwargs={'pk': 1})
        )
        statuses = Status.objects.all()
        self.assertEqual(len(statuses), 0)