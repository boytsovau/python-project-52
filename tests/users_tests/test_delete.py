from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from task_manager.users.models import TaskUser as User
from task_manager.status.models import Status
from task_manager.task.models import Task
from django.contrib.messages import get_messages
from tests import FIXTURE_DIR


class Delete(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db.json"]

    def test_delete_without_login(self):
        users_count_before = User.objects.all().count()

        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': 1}
            )
        )

        self.assertRedirects(response, reverse('user_login'))

        users_count_after = User.objects.all().count()
        self.assertEqual(users_count_after, users_count_before)

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Пожалуйста войдите для удаления пользователя',
                      [msg.message for msg in messages])

    def test_delete_only_himself(self):
        user1 = User.objects.all().first()
        user2 = User.objects.create_user(username='john', password='smith')
        self.client.login(username='john', password='smith')
        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': user1.id}
            )
        )
        self.assertRedirects(response, reverse('user_list'))
        self.assertIn(user1, User.objects.all())
        self.assertEqual(User.objects.all().count(), 2)
        self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': user2.id}
            )
        )
        self.assertEqual(User.objects.all().count(), 1)
        self.assertNotIn(user2, User.objects.all())

        messages = list(get_messages(response.wsgi_request))
        self.assertIn('У вас нет прав для изменения другого пользователя.',
                      [msg.message for msg in messages])

    def test_delete_with_tasks(self):
        status = Status(name='open status')
        user = User.objects.all()[0]
        status.save()
        task = Task(
            name="Simp Task",
            status=status,
            author=user,
        )
        task.save()
