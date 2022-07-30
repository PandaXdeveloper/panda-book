from core.apps.common.views import ActionModelMixin
from core.apps.product.filters.book import BookFilter
from core.apps.product.models import Book
from core.apps.product.serializers.book import (
    BookListSerializer,
    BookRetrieveSerializer,
    BookWriteSerializer,
)
from rest_framework import viewsets


class BookViewSet(ActionModelMixin, viewsets.ModelViewSet):
    queryset = Book.objects.select_related('category')
    list_serializer_class = BookListSerializer
    retrieve_serializer_class = BookRetrieveSerializer
    write_serializer_class = BookWriteSerializer
    filterset_class = BookFilter
