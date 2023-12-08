from users.forms import RegisterUserForm
from .testcase import UserTestCase


class UserFormTest(UserTestCase):
    def test_valid_form(self) -> None:
        user_data = self.test_user['create']['valid'].copy()
        form = RegisterUserForm(data=user_data)

        self.assertTrue(form.is_valid())

    def test_invalid_form(self) -> None:
        user_data = self.test_user['create']['missing_fields'].copy()
        form = RegisterUserForm(data=user_data)

        self.assertFalse(form.is_valid())
        