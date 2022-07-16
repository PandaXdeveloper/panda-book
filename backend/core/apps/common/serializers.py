from drf_writable_nested.mixins import NestedCreateMixin, NestedUpdateMixin
from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers


class FlexFieldsWritableNestedModelSerializer(
    FlexFieldsSerializerMixin,
    NestedCreateMixin,
    NestedUpdateMixin,
    serializers.ModelSerializer,
):
    pass
