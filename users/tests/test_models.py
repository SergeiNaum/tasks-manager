from django.test import TestCase

from task_manager.helpers import load_data
from users.models import User


class UserModelTest(TestCase):
    test_user = load_data("test_user.json")

    def test_user_creation(self) -> None:
        user_data = self.test_user["create"]["valid"].copy()
        full_name = user_data["first_name"] + " " + user_data["last_name"]

        user = User.objects.create(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
        )

        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.fullname, full_name)
        self.assertEqual(user.username, user_data["username"])
        self.assertEqual(user.first_name, user_data["first_name"])
        self.assertEqual(user.last_name, user_data["last_name"])
