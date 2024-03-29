from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.utils.translation import gettext as _
from task_manager.mark.models import Mark
from tests import FIXTURE_DIR


class UpdateStatus(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_mark.json"]

    def test_update_open_without_login(self):
        response = self.client.get(reverse('mark_update', kwargs={'pk': 1}), follow=True)
        self.assertEqual(response.status_code, 200)

        expected_message = _('Please login')
        self.assertContains(response, expected_message)

    def test_update_mark(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('mark_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('mark_update', kwargs={'pk': 1}),
            {'name': 'test'},
            follow=True
        )
        mark = Mark.objects.get(pk=1)
        self.assertEqual(mark.name, 'test')

        expected_message = _('Mark updated successfully')
        self.assertContains(response, expected_message)
