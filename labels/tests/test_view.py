from http import HTTPStatus

from django.urls import reverse_lazy
from django.test import TestCase, Client

from labels.models import Label
from users.models import User


class TestListLabels(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "test_user", "password": "te$t_pa$$word"}
        self.user = User.objects.create_user(**self.credentials)
        self.client.force_login(self.user)
        self.count = Label.objects.count()
        self.labels = Label.objects.all()

    def test_labels_view(self) -> None:
        response = self.client.get(reverse_lazy("labels:all_labels"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template_name="labels/labels.html")

    def test_labels_content(self) -> None:
        response = self.client.get(reverse_lazy("labels:all_labels"))

        self.assertEqual(len(response.context["labels"]), self.count)
        self.assertQuerysetEqual(response.context["labels"], self.labels, ordered=False)

    def test_labels_links(self) -> None:
        response = self.client.get(reverse_lazy("labels:all_labels"))

        self.assertContains(response, "/labels/create/")

        for pk in range(1, self.count + 1):
            self.assertContains(response, f"/labels/{pk}/update/")
            self.assertContains(response, f"/labels/{pk}/delete/")

    def test_labels_not_logged_in_view(self) -> None:
        self.client.logout()

        response = self.client.get(reverse_lazy("labels:all_labels"))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy("users:login"))


class TestCreateLabelView(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "test_user", "password": "te$t_pa$$word"}
        self.user = User.objects.create_user(**self.credentials)
        self.client.force_login(self.user)

    def test_create_label_view(self) -> None:
        response = self.client.get(reverse_lazy("labels:label_create"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(
            response, template_name="labels/labels_form.html"
        )  # noqa E501

    def test_create_label_not_logged_in_view(self) -> None:
        self.client.logout()

        response = self.client.get(reverse_lazy("labels:label_create"))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy("users:login"))


class TestUpdateLabelView(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "test_user", "password": "te$t_pa$$word"}
        self.user = User.objects.create_user(**self.credentials)
        self.client.force_login(self.user)

        self.status1 = Label.objects.create(pk=1, name="Blog")
        self.status2 = Label.objects.create(pk=2, name="Study")
        self.status3 = Label.objects.create(pk=3, name="Urgent")

    def test_update_label_view(self) -> None:
        response = self.client.get(
            reverse_lazy("labels:label_update", kwargs={"pk": 2})
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(
            response, template_name="labels/labels_form.html"
        )  # noqa E501

    def test_update_not_logged_in_view(self) -> None:
        self.client.logout()

        response = self.client.get(
            reverse_lazy("labels:label_update", kwargs={"pk": 2})
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy("users:login"))


class TestDeleteLabelView(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "test_user", "password": "te$t_pa$$word"}
        self.user = User.objects.create_user(**self.credentials)
        self.client.force_login(self.user)

        self.status1 = Label.objects.create(pk=1, name="Blog")
        self.status2 = Label.objects.create(pk=2, name="Study")
        self.status3 = Label.objects.create(pk=3, name="Urgent")

    def test_delete_label_view(self) -> None:
        response = self.client.get(
            reverse_lazy("labels:label_delete", kwargs={"pk": 3})
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template_name="labels/delete.html")

    def test_delete_label_not_logged_in_view(self) -> None:
        self.client.logout()

        response = self.client.get(
            reverse_lazy("labels:label_delete", kwargs={"pk": 3})
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy("users:login"))
