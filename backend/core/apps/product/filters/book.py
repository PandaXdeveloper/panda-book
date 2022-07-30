from core.apps.product.models import Book
from django_filters import FilterSet, filters


class BookFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='icontains', label='Book name')
    author = filters.CharFilter(lookup_expr='icontains', label='Author name')

    class Meta:
        model = Book
        fields = [
            'name',
            'author',
        ]
