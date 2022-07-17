from core.apps.authentication.models import User
from core.apps.authentication.serializers.account import CreateAccountSerializer
from core.apps.common.views import CreateOnlyModelViewSet


class CreateAccountViewSet(CreateOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateAccountSerializer
