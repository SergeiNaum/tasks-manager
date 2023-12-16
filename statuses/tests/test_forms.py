from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse

from statuses.forms import StatusForm
from task_manager.helpers import load_data
from users.models import User


class TasksTestCase(TestCase):
    # fixtures = ['user.json', 'status.json', 'task.json', 'label.json']
    test_status = load_data("test_status.json")

    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "test_user", "password": "te$t_pa$$word"}
        self.user = User.objects.create_user(**self.credentials)

    def test_form_get(self):
        self.client.force_login(self.user)
        path = reverse("statuses:status_create")
        response = self.client.get(path)
        self.assertTemplateUsed(response, "statuses/statuses_form.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_tasks_create(self):
        self.client.force_login(self.user)
        path = reverse("statuses:status_create")
        response = self.client.post(path, self.test_status)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_valid_form(self) -> None:
        status_data = self.test_status["create"]["valid"].copy()
        form = StatusForm(data=status_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self) -> None:
        status_data = self.test_status["create"]["missing_fields"].copy()
        form = StatusForm(data=status_data)

        self.assertFalse(form.is_valid())
