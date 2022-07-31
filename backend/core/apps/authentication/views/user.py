from core.apps.authentication.models import User
from core.apps.authentication.serializers.user import (
    UserListSerializer,
    UserWriteSerializer,
)
from core.apps.common.views import ActionModelMixin
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(ActionModelMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    list_serializer_class = UserListSerializer
    write_serializer_class = UserWriteSerializer

    @action(methods=['get'], detail=False, url_path='current')
    def current(self, request):
        serializer = UserListSerializer(request.user)
        return Response(serializer.data)
