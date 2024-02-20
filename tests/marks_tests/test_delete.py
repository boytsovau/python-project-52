from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.utils.translation import gettext as _
from task_manager.mark.models import Mark
from tests import FIXTURE_DIR


class DeleteMark(TestCase):
    fixtures = [f"{FIXTURE_DIR}/db_mark.json"]

    def test_delete_open_without_login(self):
        response = self.client.get(reverse('mark_delete', kwargs={'pk': 1}), 
                                   follow=True)
        self.assertEqual(response.status_code, 200)

        expected_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')
        self.assertContains(response, expected_message)

    def test_delete_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('mark_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('mark_delete', kwargs={'pk': 1}),
            follow=True
        )
        statuses = Mark.objects.all()
        self.assertEqual(len(statuses), 0)

        expected_message = _('Метка успешно удалена')
        self.assertContains(response, expected_message)
