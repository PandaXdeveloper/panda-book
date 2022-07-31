from django.db import models
from django.utils.translation import gettext_lazy as _


class BookCoverType(models.TextChoices):
    SOFTCOVER = 'softcover', _('Softcover')
    HARDCOVER = 'hardcover', _('Hardcover')


class BookStyle(models.TextChoices):
    PAPER_BOOK = 'paper book', _('Paper Book')
    E_BOOK = 'e-book', _('E-Book')
