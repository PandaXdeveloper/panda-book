from core.apps.authentication.choices import Role
from core.apps.authentication.managers import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=8, default=Role.CUSTOMER, choices=Role.choices)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    class Meta:
        ordering = ['id']
