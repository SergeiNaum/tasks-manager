
from users.forms import RegisterUserForm
from django.test import TestCase


class UserFormTest(TestCase):

    def test_valid_form(self) -> None:
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = RegisterUserForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_invalid_form(self) -> None:
        invalid_form_data = {
            'first_name': 'Ringo',
            'last_name': 'Starr',
            'username': 'R!c h1e',
            'password1': 'p@$$w0rd',
            'password2': 'p@$$w0rd',
        }
        form = RegisterUserForm(data=invalid_form_data)

        self.assertFalse(form.is_valid())
