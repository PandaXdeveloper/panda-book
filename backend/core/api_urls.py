from rest_framework import routers

from core.apps.authentication.views.account import CreateAccountViewSet
from core.apps.authentication.views.user import UserViewSet
from core.apps.product.views.book import BookViewSet
from core.apps.product.views.book_category import BookCategoryViewSet

router = routers.DefaultRouter()
router.register('book-categories', BookCategoryViewSet, 'book-categories')
router.register('books', BookViewSet, 'books')
router.register('create-accounts', CreateAccountViewSet, 'create-accounts')
router.register('users', UserViewSet, 'users')

urlpatterns = []

urlpatterns += router.urls
