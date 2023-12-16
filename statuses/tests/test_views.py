from http import HTTPStatus

from django.urls import reverse_lazy
from django.test import TestCase, Client

from statuses.models import Status
from users.models import User


class TestListStatuses(TestCase):

    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials)
        self.client.force_login(self.user)
        self.count = Status.objects.count()
        self.statuses = Status.objects.all()

    def test_statuses_view(self) -> None:
        response = self.client.get(reverse_lazy('statuses:all_statuses'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(
            response,
            template_name='statuses/statuses.html'
        )

    def test_statuses_content(self) -> None:
        response = self.client.get(reverse_lazy('statuses:all_statuses'))

        self.assertEqual(len(response.context['statuses']), self.count)
        self.assertQuerysetEqual(
            response.context['statuses'],
            self.statuses,
            ordered=False
        )

    def test_statuses_links(self) -> None:
        response = self.client.get(reverse_lazy('statuses:all_statuses'))

        self.assertContains(response, '/statuses/create/')

        for pk in range(1, self.count + 1):
            self.assertContains(response, f'/statuses/{pk}/update/')
            self.assertContains(response, f'/statuses/{pk}/delete/')

    def test_statuses_not_logged_in_view(self) -> None:
        self.client.logout()

        response = self.client.get(reverse_lazy('statuses:all_statuses'))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy('users:login'))


class TestCreateStatusView(TestCase):

    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials)
        self.client.force_login(self.user)

    def test_create_status_view(self) -> None:
        response = self.client.get(reverse_lazy('statuses:status_create'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template_name='statuses/statuses_form.html') # noqa E501

    def test_create_status_not_logged_in_view(self) -> None:
        self.client.logout()

        response = self.client.get(reverse_lazy('statuses:status_create'))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy('users:login'))


class TestUpdateStatusView(TestCase):

    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials)
        self.client.force_login(self.user)

        self.status1 = Status.objects.create(pk=1, name='Started')
        self.status2 = Status.objects.create(pk=2, name='Paused')
        self.status3 = Status.objects.create(pk=3, name='Finished')

    def test_update_status_view(self) -> None:
        response = self.client.get(
            reverse_lazy('statuses:status_update', kwargs={'pk': 2})
        )

        self.assertEqual(response.status_code, HTTPStatus.OK) # noqa E501
        self.assertTemplateUsed(response, template_name='statuses/statuses_form.html') # noqa E501

    def test_update_not_logged_in_view(self) -> None:
        self.client.logout()

        response = self.client.get(
            reverse_lazy('statuses:status_update', kwargs={'pk': 2})
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy('users:login'))


class TestDeleteStatusView(TestCase):

    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials)
        self.client.force_login(self.user)

        self.status1 = Status.objects.create(pk=1, name='Started')
        self.status2 = Status.objects.create(pk=2, name='Paused')
        self.status3 = Status.objects.create(pk=3, name='Finished')

    def test_delete_status_view(self) -> None:
        response = self.client.get(
            reverse_lazy('statuses:status_delete', kwargs={'pk': 3})
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template_name='statuses/delete.html')

    def test_delete_status_not_logged_in_view(self) -> None:
        self.client.logout()

        response = self.client.get(
            reverse_lazy('statuses:status_delete', kwargs={'pk': 3})
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy('users:login'))
