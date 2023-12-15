from django.test import TestCase, Client

from django.utils import timezone

from labels.models import Label
from statuses.models import Status
from task_manager.helpers import load_data
from tasks.models import Task
from users.models import User


class TasksModelTest(TestCase):
    test_task = load_data('test_task.json')

    def setUp(self):
        self.client = Client()

        self.credentials1 = {
            'username': 'test_user',
            'password': 'te$t_pa$$word'
        }
        self.credentials2 = {
            'username': 'test_user2',
            'password': 'te$t_pa$$word'
        }
        self.user = User.objects.create_user(**self.credentials1)
        self.user2 = User.objects.create_user(**self.credentials2)
        self.client.force_login(self.user)

    def test_tasks_creation(self) -> None:
        task_data = self.test_task['create']['valid'].copy()
        self.status1 = Status.objects.create(name='in_work')
        self.label2 = Label.objects.create(pk=2, name='slowly')
        self.labels = Label.objects.filter(pk=2)

        task = Task.objects.create(
            name=task_data['name'],
            description=task_data['description'],
            created_at=timezone.now(),
            author=self.user,
            status=self.status1,
            executor=self.user2,
        )
        task.labels.set(self.labels)

        self.assertTrue(isinstance(task, Task))
        self.assertEqual(task.__str__(), task_data['name'])
        self.assertEqual(task.name, task_data['name'])
        self.assertEqual(task.description, task_data['description'])
        self.assertEqual(task.author, self.user)
        self.assertEqual(task.status, self.status1)
        self.assertEqual(task.executor, self.user2)
        self.assertEqual(task.labels.get(pk=2), self.label2)
