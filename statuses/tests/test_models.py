from django.test import TestCase, Client

from django.utils import timezone

from statuses.models import Status
from task_manager.helpers import load_data
from users.models import User


class StatusModelTest(TestCase):
    test_status = load_data('test_status.json')

    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_status_creation(self) -> None:
        status_data = self.test_status['create']['valid'].copy()

        status = Status.objects.create(
            name=status_data['name'],
            created_at=timezone.now()
        )

        self.assertTrue(isinstance(status, Status))
        self.assertEqual(status.__str__(), status_data['name'])
        self.assertEqual(status.name, status_data['name'])
