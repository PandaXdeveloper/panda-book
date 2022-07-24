from core.apps.common.views import ActionModelMixin
from core.apps.product.models import BookCategory
from core.apps.product.serializers.book_category import (
    BookCategoryListSerializer,
    BookCategoryWriteSerializer,
)
from rest_framework import viewsets


class BookCategoryViewSet(ActionModelMixin, viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    list_serializer_class = BookCategoryListSerializer
    write_serializer_class = BookCategoryWriteSerializer
