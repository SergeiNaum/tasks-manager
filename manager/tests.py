from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse

from users.models import User


class GetPagesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_mainpage(self):
        path = reverse('index')
        response = self.client.get(path)
        expected = response.status_code
        self.assertEqual(expected, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'manager/index.html')
        self.assertEqual(response.context_data['title'], 'Task Manager')

    def test_header_links_logged_in(self) -> None:
        self.client.force_login(self.user)
        response = self.client.get(reverse('index'))

        self.assertContains(response, '/users/')
        self.assertContains(response, '/statuses/')
        self.assertContains(response, '/labels/')
        self.assertContains(response, '/tasks/')
        self.assertContains(response, '/logout/')
        self.assertNotContains(response, '/login/')

    def test_header_links_not_logged_in(self) -> None:
        response = self.client.get(reverse('index'))

        self.assertContains(response, '/users/')
        self.assertContains(response, '/login/')

        self.assertNotContains(response, '/statuses/')
        self.assertNotContains(response, '/labels/')
        self.assertNotContains(response, '/tasks/')
        self.assertNotContains(response, '/logout/')


class TestLoginUser(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_user_login_view(self) -> None:
        response = self.client.get(reverse('users:login'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template_name='users/login.html')

    def test_user_login(self) -> None:
        response = self.client.post(
            reverse('users:login'),
            self.credentials,
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(response.context['user'].is_authenticated)


class TestLogoutUser(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_user_logout(self) -> None:
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('users:logout'),
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('index'))
        self.assertFalse(response.context['user'].is_authenticated)
