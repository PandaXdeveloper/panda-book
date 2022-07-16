from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.TextChoices):
    ADMIN = 'admin', _('Admin')
    STAFF = 'staff', _('Staff')
    CUSTOMER = 'customer', _('Customer')
