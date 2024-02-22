from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from django.utils.translation import gettext as _
from task_manager.users.models import TaskUser as User
from tests import FIXTURE_DIR, load_fixture_data


class Delete(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db.json"]

    def test_delete_without_login(self):
        users_count_before = User.objects.all().count()

        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': 1}
            ),
            follow=True
        )

        self.assertRedirects(response, reverse('user_login'))

        users_count_after = User.objects.all().count()
        self.assertEqual(users_count_after, users_count_before)

        expected_message = _('Please login to delete user')
        self.assertContains(response, expected_message)

    def test_delete_only_himself(self):
        user1 = User.objects.all().first()
        user2_data = load_fixture_data('user.json')
        user2 = User.objects.create_user(username=user2_data.get('username'),
                                         password=user2_data.get('password'))
        self.client.login(username=user2_data['username'],
                          password=user2_data['password'])
        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': user1.id}
            ),
            follow=True
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

        expected_message = _('You cannot edit another user')
        self.assertContains(response, expected_message)
