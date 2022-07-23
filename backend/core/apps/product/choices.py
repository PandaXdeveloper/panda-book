from django.db import models
from django.utils.translation import gettext_lazy as _


class CoverType(models.TextChoices):
    SOFTCOVER = 'softcover', _('Softcover')
    HARDCOVER = 'hardcover', _('Hardcover')
