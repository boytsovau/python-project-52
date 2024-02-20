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

        expected_message = _('Пользователь не может быть удален, так как используется')
        self.assertContains(response, expected_message)

    def test_delete_after_modify_task(self):
        user1 = User.objects.all().first()
        user2 = User.objects.all().last()
        task = Task.objects.all().first()
        self.assertEqual(Task.objects.all().count(), 1)
        task.author = user2
        task.performer = user2
        task.save()
        self.client.force_login(user=user1)
        self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': user1.id}
            )
        )
        self.assertEqual(User.objects.all().count(), 1)
