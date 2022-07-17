from rest_framework import routers

from core.apps.authentication.views.account import CreateAccountViewSet

router = routers.DefaultRouter()
router.register('create-accounts', CreateAccountViewSet, 'create-accounts')

urlpatterns = []

urlpatterns += router.urls
