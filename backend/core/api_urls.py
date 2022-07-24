from rest_framework import routers

from core.apps.authentication.views.account import CreateAccountViewSet
from core.apps.product.views.book_category import BookCategoryViewSet

router = routers.DefaultRouter()
router.register('book-categories', BookCategoryViewSet, 'book-categories')
router.register('create-accounts', CreateAccountViewSet, 'create-accounts')

urlpatterns = []

urlpatterns += router.urls
