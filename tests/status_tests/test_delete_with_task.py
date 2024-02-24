from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from task_manager.status.models import Status
from django.utils.translation import gettext as _
from tests import FIXTURE_DIR


class DeleteStutusWithTask(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db_task_two_users.json"]

    def test_delete_with_task(self):
        status = Status.objects.all().first()
        user = User.objects.all().first()
        self.assertEqual(Status.objects.all().count(), 1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('status_delete',
                                   kwargs={'pk': status.id}))
        self.assertEqual(Status.objects.all().count(), 1)
        expected_message = _("Are you sure delete")
        self.assertContains(response, expected_message)
