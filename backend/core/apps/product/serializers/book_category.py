from core.apps.common.serializers import FlexFieldsWritableNestedModelSerializer
from core.apps.product.models import BookCategory


class BookCategoryListSerializer(FlexFieldsWritableNestedModelSerializer):
    class Meta:
        model = BookCategory
        fields = [
            'id',
            'name',
        ]


class BookCategoryWriteSerializer(FlexFieldsWritableNestedModelSerializer):
    class Meta:
        model = BookCategory
        fields = [
            'name',
        ]
