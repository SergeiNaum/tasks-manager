from django.test import TestCase, Client
from django.utils import timezone

from labels.models import Label
from task_manager.helpers import load_data
from users.models import User


class LabelModelTest(TestCase):
    test_label = load_data('test_label.json')

    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_label_creation(self) -> None:
        label_data = self.test_label['create']['valid'].copy()

        label = Label.objects.create(
            name=label_data['name'],
            created_at=timezone.now()
        )

        self.assertTrue(isinstance(label, Label))
        self.assertEqual(label.__str__(), label_data['name'])
        self.assertEqual(label.name, label_data['name'])
