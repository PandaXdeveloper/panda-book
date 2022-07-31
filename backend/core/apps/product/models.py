from decimal import Decimal

from core.apps.product.choices import BookCoverType, BookStyle
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class BookCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']


class Book(models.Model):
    category = models.ForeignKey(to=BookCategory, on_delete=models.CASCADE, related_name='books')
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    cover_type = models.CharField(max_length=9, choices=BookCoverType.choices, blank=True)
    normal_price = models.DecimalField(max_digits=7, decimal_places=2)
    percentage_discount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(limit_value=0), MaxValueValidator(limit_value=100)]
    )
    total_quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    barcode = models.CharField(max_length=13)
    isbn = models.CharField(max_length=13, blank=True)
    year_of_print = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=50, blank=True)
    number_of_page = models.CharField(max_length=50, blank=True)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to='book/image/%Y-%m-%d')
    style = models.CharField(max_length=10, choices=BookStyle.choices)

    @property
    def special_price(self):
        return Decimal(
            round(
                self.normal_price - (self.normal_price * Decimal(self.percentage_discount / 100))
            )
        )

    class Meta:
        ordering = ['id']
