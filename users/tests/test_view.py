from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse_lazy

from users.models import User


class TestListUsers(TestCase):

    def setUp(self):
        self.client = Client()
        self.credentials1 = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }

        self.credentials2 = {
            'username': 'test_user2',
            'password': 'te$t_pa$$word2'
        }

        self.credentials3 = {
            'username': 'test_user3',
            'password': 'te$t_pa$$word3'
        }

        self.user1 = User.objects.create_user(**self.credentials1)
        self.user2 = User.objects.create_user(**self.credentials2)
        self.user3 = User.objects.create_user(**self.credentials3)
        self.users = User.objects.all()
        self.count = User.objects.count()

    def test_users_view(self) -> None:
        response = self.client.get(reverse_lazy('users:users_index'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template_name='users/all_users.html')

    def test_users_content(self) -> None:
        response = self.client.get(reverse_lazy('users:users_index'))

        self.assertEqual(len(response.context['users']), self.count)
        self.assertQuerysetEqual(
            response.context['users'],
            self.users,
            ordered=False
        )

    def test_users_links(self) -> None:
        response = self.client.get(reverse_lazy('users:users_index'))

        self.assertContains(response, '/users/create/')

        for pk in range(1, self.count + 1):
            self.assertContains(response, f'/users/{pk}/update/')
            self.assertContains(response, f'/users/{pk}/delete/')


class TestCreateUserView(TestCase):
    def test_sign_up_view(self) -> None:
        response = self.client.get(reverse_lazy('users:register'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template_name='users/register.html')


class TestUpdateUserView(TestCase):

    def setUp(self):
        self.client = Client()
        self.credentials1 = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }

        self.credentials2 = {
            'username': 'test_user2',
            'password': 'te$t_pa$$word2'
        }

        self.credentials3 = {
            'username': 'test_user3',
            'password': 'te$t_pa$$word3'
        }

        self.user1 = User.objects.create_user(**self.credentials1)
        self.user2 = User.objects.create_user(**self.credentials2)
        self.user3 = User.objects.create_user(**self.credentials3)
        self.users = User.objects.all()
        self.count = User.objects.count()

    def test_update_self_view(self) -> None:
        self.client.force_login(self.user2)

        response = self.client.get(
            reverse_lazy('users:edit_user', kwargs={'pk': 2})
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template_name='users/edit_user_form.html')  # noqa E501

    def test_update_not_logged_in_view(self) -> None:
        self.client.logout()
        response = self.client.get(
            reverse_lazy('users:edit_user', kwargs={'pk': 2})
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy('users:login'))

    def test_update_other_view(self) -> None:
        self.client.force_login(self.user1)

        response = self.client.get(
            reverse_lazy('users:edit_user', kwargs={'pk': 2})
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy('users:users_index'))
