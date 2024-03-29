from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from django.utils.translation import gettext as _
from task_manager.users.models import TaskUser as User
from tests import FIXTURE_DIR, load_fixture_data


class Modify(TransactionTestCase):
    fixtures = [f"{FIXTURE_DIR}/db.json"]

    def setUp(self):
        self.TEST_USER = load_fixture_data('user.json')
        self.username = self.TEST_USER.get('username')
        self.password = self.TEST_USER.get('password')

    def test_modify_only_logged(self):
        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': 1}
            ),
            self.TEST_USER,
            follow=True
        )
        self.assertRedirects(response, reverse('user_login'))
        expected_message = _('Please login to modify user')
        self.assertContains(response, expected_message)

    def test_modify_redirect_after_logging(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': user.id}
            ),
            self.TEST_USER
        )
        self.assertRedirects(response, reverse('user_list'))
        user = User.objects.get(pk=user.id)
        self.assertEqual(user.first_name, self.TEST_USER.get('first_name'))
        self.assertEqual(user.last_name, self.TEST_USER.get('last_name'))
        self.assertEqual(user.username, self.TEST_USER.get('username'))

    def test_modify_only_himself(self):
        self.assertEqual(User.objects.all().count(), 1)
        user1 = User.objects.all().first()
        testuser = User.objects.create_user(username=self.username,
                                            password=self.password)
        self.assertEqual(User.objects.all().count(), 2)

        self.client.force_login(user=testuser)
        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': user1.id}
            ),
            self.TEST_USER,
            follow=True
        )
        self.assertRedirects(response, reverse('user_list'))
        user = User.objects.get(pk=user1.id)
        self.assertEqual(user1, user)

        expected_message = _('You cannot edit another user')
        self.assertContains(response, expected_message)
