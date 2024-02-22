from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from task_manager.users.models import TaskUser as User
from task_manager.task.models import Task
from django.utils.translation import gettext as _
from tests import FIXTURE_DIR


class Remove(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db_task_two_users.json"]

    def test_delete_with_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': user.id}
            ),
            follow=True
        )
        self.assertRedirects(response, reverse('user_list'))
        self.assertEqual(User.objects.all().count(), 2)

        expected_message = _("User can't be deleted - on use now")
        self.assertContains(response, expected_message)

    def test_delete_after_modify_task(self):
        self.user1 = User.objects.all().first()
        self.user2 = User.objects.all().last()
        self.task = Task.objects.all().first()
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(self.task.author, self.user1)
        self.assertEqual(self.task.executor, self.user2)

        self.client.force_login(user=self.user2)
        response = self.client.post(
            reverse('user_delete', kwargs={'pk': self.user1.pk}),
            follow=True
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(Task.objects.count(), 1)

        self.task.refresh_from_db()
        self.assertEqual(self.task.author, self.user1)
        self.assertEqual(self.task.executor, self.user2)
        expected_message = _("You cannot edit another user")
        self.assertContains(response, expected_message)
