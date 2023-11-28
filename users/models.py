from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'


