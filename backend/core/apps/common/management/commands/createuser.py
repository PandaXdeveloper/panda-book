import getpass
import sys

from core.apps.authentication.choices import Role
from core.apps.authentication.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Used to create a superuser.'

    def handle(self, *args, **options):
        try:
            name = input('name: ')
            surname = input('surname: ')
            birthday = input('birthday: ')
            email = input('email: ')
            password = getpass.getpass('password: ')
            User.objects.create_user(
                name=name,
                surname=surname,
                birthday=birthday,
                email=email,
                password=password,
                role=Role.ADMIN,
                is_staff=True,
                is_superuser=True,
            )
        except KeyboardInterrupt:
            self.stderr.write('\nOperation cancelled.')
            sys.exit(1)
