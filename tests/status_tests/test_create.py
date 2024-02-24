from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.utils.translation import gettext as _
from task_manager.status.models import Status
from tests import FIXTURE_DIR, load_fixture_data


class Create(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_status.json"]

    def setUp(self):
        self.TEST_STATUS = load_fixture_data('data.json')
        self.status_name = self.TEST_STATUS.get('status').get('name')

    def test_create_open_without_login(self):
        response = self.client.get(reverse('status_add'), follow=True)
        self.assertEqual(response.status_code, 200)

        expected_message = _('Please login')
        self.assertContains(response, expected_message)

    def test_create_task(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        initial_status_count = Status.objects.all().count()
        response = self.client.get(reverse('status_add'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('status_add'),
            {'name': self.status_name},
            follow=True
        )
        self.assertEqual(Status.objects.all().count(),
                         initial_status_count + 1)

        expected_message = _('Status created successfully')
        self.assertContains(response, expected_message)
