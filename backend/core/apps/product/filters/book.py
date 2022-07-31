from core.apps.product.choices import BookStyle
from core.apps.product.models import Book
from django_filters import FilterSet, filters


class BookFilter(FilterSet):
    book_name = filters.CharFilter(field_name='name', lookup_expr='icontains', label='Book name')
    author_name = filters.CharFilter(
        field_name='author', lookup_expr='icontains', label='Author name'
    )
    book_style = filters.ChoiceFilter(
        field_name='style', choices=BookStyle.choices, label='Book style'
    )

    class Meta:
        model = Book
        fields = [
            'book_name',
            'author_name',
            'book_style',
        ]
