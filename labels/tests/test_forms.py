from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse

from labels.forms import LabelForm
from task_manager.helpers import load_data
from users.models import User


class LabelFormTest(TestCase):
    test_label = load_data('test_label.json')

    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_form_get(self):
        self.client.force_login(self.user)
        path = reverse('labels:label_create')
        response = self.client.get(path)
        self.assertTemplateUsed(response, 'labels/labels_form.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_statuses_create(self):
        self.client.force_login(self.user)
        path = reverse('labels:label_create')
        response = self.client.post(path, self.test_label)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_valid_form(self) -> None:
        label_data = self.test_label['create']['valid'].copy()
        form = LabelForm(data=label_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self) -> None:
        label_data = self.test_label['create']['missing_fields'].copy()
        form = LabelForm(data=label_data)
        self.assertFalse(form.is_valid())
