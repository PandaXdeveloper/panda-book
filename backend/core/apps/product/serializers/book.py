from core.apps.common.serializers import FlexFieldsWritableNestedModelSerializer
from core.apps.product.models import Book
from core.apps.product.serializers.book_category import BookCategoryListSerializer
from rest_framework import serializers


class BookListSerializer(FlexFieldsWritableNestedModelSerializer):
    normal_price = serializers.DecimalField(max_digits=7, decimal_places=2)
    special_price = serializers.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        model = Book
        fields = [
            'id',
            'image',
            'name',
            'author',
            'normal_price',
            'special_price',
        ]


class BookRetrieveSerializer(FlexFieldsWritableNestedModelSerializer):
    category = BookCategoryListSerializer()
    cover_type_display = serializers.CharField(source='get_cover_type_display')
    normal_price = serializers.DecimalField(max_digits=7, decimal_places=2)
    special_price = serializers.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        model = Book
        fields = [
            'id',
            'category',
            'name',
            'author',
            'cover_type',
            'cover_type_display',
            'normal_price',
            'percentage_discount',
            'special_price',
            'total_quantity',
            'barcode',
            'isbn',
            'year_of_print',
            'size',
            'number_of_page',
            'detail',
            'image',
        ]


class BookWriteSerializer(FlexFieldsWritableNestedModelSerializer):
    class Meta:
        model = Book
        fields = [
            'category',
            'name',
            'author',
            'cover_type',
            'normal_price',
            'percentage_discount',
            'total_quantity',
            'barcode',
            'isbn',
            'year_of_print',
            'size',
            'number_of_page',
            'detail',
            'image',
        ]
