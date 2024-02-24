from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.utils.translation import gettext as _
from task_manager.mark.models import Mark
from tests import FIXTURE_DIR, load_fixture_data


class Create(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_mark.json"]

    def setUp(self):
        self.TEST_MARK = load_fixture_data('data.json')
        self.mark_name = self.TEST_MARK.get('mark').get('name')

    def test_create_open_without_login(self):
        response = self.client.get(reverse('mark_add'), follow=True)
        self.assertEqual(response.status_code, 200)

        expected_message = _('Please login')
        self.assertContains(response, expected_message)

    def test_create_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('mark_add'))
        self.assertEqual(response.status_code, 200)
        initial_marks_count = Mark.objects.all().count()
        response = self.client.post(
            reverse('mark_add'),
            {'name':  self.mark_name},
            follow=True
        )
        self.assertEqual(Mark.objects.all().count(), initial_marks_count + 1)

        expected_message = _('Mark created successfully')
        self.assertContains(response, expected_message)
