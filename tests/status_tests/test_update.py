from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.utils.translation import gettext as _
from task_manager.status.models import Status
from tests import FIXTURE_DIR


class UpdateStatus(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_status.json"]

    def test_update_open_without_login(self):
        response = self.client.get(reverse('status_update', kwargs={'pk': 1}), 
                                   follow=True)
        self.assertEqual(response.status_code, 200)

        expected_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')
        self.assertContains(response, expected_message)

    def test_update_task(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('status_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('status_update', kwargs={'pk': 1}),
            {'name': 'test'}
        )
        status = Status.objects.get(pk=1)
        self.assertEqual(status.name, 'test')
