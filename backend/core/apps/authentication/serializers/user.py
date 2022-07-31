from core.apps.authentication.models import User
from core.apps.common.serializers import FlexFieldsWritableNestedModelSerializer
from rest_framework import serializers


class UserListSerializer(FlexFieldsWritableNestedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'birthday',
            'email',
        ]


class UserWriteSerializer(FlexFieldsWritableNestedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'birthday',
            'email',
            'password',
            'role',
            'is_staff',
            'is_active',
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
