from http import HTTPStatus

from django.urls import reverse_lazy
from django.test import TestCase, Client
from labels.models import Label
from statuses.models import Status
from tasks.models import Task
from users.models import User


class TestListTasks(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "test_user", "password": "te$t_pa$$word"}
        self.user = User.objects.create_user(**self.credentials)
        self.client.force_login(self.user)
        self.count = Task.objects.count()
        self.tasks = Task.objects.all()

    def test_tasks_view(self) -> None:
        response = self.client.get(reverse_lazy("tasks:tasks"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template_name="tasks/tasks.html")

    def test_tasks_links(self) -> None:
        response = self.client.get(reverse_lazy("tasks:tasks"))

        self.assertContains(response, "/tasks/create/")

        for pk in range(1, self.count + 1):
            self.assertContains(response, f"/tasks/{pk}/update/")
            self.assertContains(response, f"/tasks/{pk}/delete/")

    def test_statuses_not_logged_in_view(self) -> None:
        self.client.logout()

        response = self.client.get(reverse_lazy("tasks:tasks"))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy("users:login"))


class TestCreateTasksView(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "test_user", "password": "te$t_pa$$word"}
        self.user = User.objects.create_user(**self.credentials)
        self.client.force_login(self.user)

    def test_create_tasks_view(self) -> None:
        response = self.client.get(reverse_lazy("tasks:task_create"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(
            response, template_name="tasks/tasks_form.html"
        )  # noqa E501

    def test_create_tasks_not_logged_in_view(self) -> None:  # noqa E501
        self.client.logout()

        response = self.client.get(reverse_lazy("tasks:task_create"))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy("users:login"))


class TestTaskEditView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="12345"
        )  # noqa E501
        self.client.login(username="testuser", password="12345")
        self.status1 = Status.objects.create(name="in_work")  # noqa E501
        self.executor = User.objects.create_user(
            username="executor", password="executorpass"
        )  # noqa E501
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            author=self.user,
            executor=self.executor,
            status=self.status1,
        )

    def test_task_edit_view(self):
        response = self.client.get(
            reverse_lazy("tasks:task_update", kwargs={"pk": self.task.pk})
        )  # noqa E501
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(
            response, template_name="tasks/tasks_form.html"
        )  # noqa E501

    def test_update_not_logged_in_view(self) -> None:  # noqa E501
        self.client.logout()

        response = self.client.get(reverse_lazy("tasks:task_update", kwargs={"pk": 2}))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy("users:login"))


class TestDeleteStatusView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="12345"
        )  # noqa E501
        self.client.login(username="testuser", password="12345")  # noqa E501
        self.status1 = Status.objects.create(name="in_work")  # noqa E501
        self.executor = User.objects.create_user(
            username="executor", password="executorpass"
        )  # noqa E501
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            author=self.user,
            executor=self.executor,
            status=self.status1,
        )

    def test_delete_task_view(self) -> None:
        response = self.client.get(
            reverse_lazy("tasks:task_delete", kwargs={"pk": 1})  # noqa E501
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(
            response, template_name="tasks/delete.html"
        )  # noqa E501

    def test_delete_status_not_logged_in_view(self) -> None:
        self.client.logout()

        response = self.client.get(reverse_lazy("tasks:task_delete", kwargs={"pk": 3}))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy("users:login"))


class TestDetailedTask(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="12345"
        )  # noqa E501
        self.client.login(username="testuser", password="12345")
        self.status1 = Status.objects.create(name="in_work")
        self.executor = User.objects.create_user(
            username="executor", password="executorpass"
        )  # noqa E501
        self.label1 = Label.objects.create(pk=2, name="slowly")
        self.labels = Label.objects.filter(pk=2)
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            author=self.user,
            executor=self.executor,
            status=self.status1,
        )

        self.task.labels.set(self.labels)

    def test_detailed_task_view(self) -> None:
        response = self.client.get(reverse_lazy("tasks:task_show", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template_name="tasks/task_detail.html")

    def test_detailed_task_content(self) -> None:
        response = self.client.get(reverse_lazy("tasks:task_show", kwargs={"pk": 1}))

        labels = self.task.labels.all()

        self.assertContains(response, "/tasks/1/update/")
        self.assertContains(response, "/tasks/1/delete/")

        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.description)
        self.assertContains(response, self.task.author)
        self.assertContains(response, self.task.executor)
        self.assertContains(response, self.task.status)

        for label in labels:
            self.assertContains(response, label.name)

    def test_detailed_task_not_logged_in(self) -> None:
        self.client.logout()

        response = self.client.get(reverse_lazy("tasks:task_show", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy("users:login"))
