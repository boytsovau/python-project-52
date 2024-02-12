from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from task_manager.mark.models import Mark
import os

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../fixtures'
)


class DeleteMarkWithTask(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db_mark_with_bond.json"]

    def test_delete_with_mark(self):
        mark = Mark.objects.all().first()
        user = User.objects.all().first()
        self.assertEqual(Mark.objects.all().count(), 1)
        self.client.force_login(user=user)
        self.client.get(reverse('mark_delete',
                                kwargs={'pk': mark.id}))
        self.assertEqual(Mark.objects.all().count(), 1)
