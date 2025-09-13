from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManager(AbstractUser):
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.get_full_name()